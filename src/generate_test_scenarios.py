"""Create documented generated testing scenarios for the SC11 example.

These scenarios are derived from the cleaned cited data only for testing and
demonstration.  They are not additional real laboratory observations and must
not be used to train, tune, or report the final model's accuracy.
"""

from pathlib import Path
import math
import random

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "water_potability_clean.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "generated"
OUTPUT_FILE = OUTPUT_DIR / "generated_water_quality_test_scenarios.csv"
REPORT_FILE = PROJECT_ROOT / "data" / "reports" / "generated_scenarios_report.md"

FEATURE_COLUMNS = [
    "ph",
    "Hardness",
    "Solids",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic_carbon",
    "Trihalomethanes",
    "Turbidity",
]

SEED = 42
SCENARIO_RATIO = 0.10


def scenario_count_for(dataframe):
    """Return at least 10 percent of the real cleaned-record count."""
    return math.ceil(len(dataframe) * SCENARIO_RATIO)


def feature_jitter_scales(dataframe):
    """Use one percent of each feature's IQR as a small, documented jitter."""
    scales = {}
    for column in FEATURE_COLUMNS:
        interquartile_range = dataframe[column].quantile(0.75) - dataframe[column].quantile(0.25)
        if interquartile_range == 0:
            interquartile_range = dataframe[column].max() - dataframe[column].min()
        scales[column] = float(interquartile_range) * 0.01
    return scales


def generate_scenarios(cleaned_data):
    """Make balanced, slightly perturbed test-only scenarios by class."""
    total_scenarios = scenario_count_for(cleaned_data)
    label_zero_count = total_scenarios // 2
    label_one_count = total_scenarios - label_zero_count
    requested_counts = {0: label_zero_count, 1: label_one_count}
    scales = feature_jitter_scales(cleaned_data)
    random_generator = random.Random(SEED)
    scenarios = []

    for label, requested_count in requested_counts.items():
        candidates = cleaned_data.loc[cleaned_data["Potability"] == label].reset_index(drop=True)
        sampled = candidates.sample(
            n=requested_count,
            replace=True,
            random_state=SEED + label,
        ).reset_index(drop=True)

        for _, source_row in sampled.iterrows():
            scenario = {}
            for column in FEATURE_COLUMNS:
                value = float(source_row[column]) + random_generator.gauss(0, scales[column])
                minimum = float(cleaned_data[column].min())
                maximum = float(cleaned_data[column].max())
                if column == "ph":
                    minimum, maximum = 0.0, 14.0
                scenario[column] = round(min(max(value, minimum), maximum), 6)

            scenario["Expected_Potability"] = label
            scenario["Scenario_Type"] = "generated_testing_only"
            scenario["Generation_Seed"] = SEED
            scenarios.append(scenario)

    generated = pd.DataFrame(scenarios)
    generated.insert(0, "Scenario_ID", [f"GEN-WQ-{number:03d}" for number in range(1, len(generated) + 1)])
    return generated


def validate_scenarios(generated, cleaned_data):
    """Prove that scenarios are complete, valid and not copied real records."""
    expected_count = scenario_count_for(cleaned_data)
    if len(generated) != expected_count:
        raise ValueError(f"Expected {expected_count} scenarios but found {len(generated)}.")
    if generated.isna().sum().sum() != 0:
        raise ValueError("Generated scenarios contain missing values.")
    if generated["Scenario_ID"].duplicated().any():
        raise ValueError("Generated scenario IDs must be unique.")
    if generated[FEATURE_COLUMNS].duplicated().any():
        raise ValueError("Generated scenarios must not duplicate one another.")
    if not generated["ph"].between(0, 14).all():
        raise ValueError("Generated pH values must remain between 0 and 14.")
    if (generated[FEATURE_COLUMNS] < 0).sum().sum() != 0:
        raise ValueError("Generated scenarios contain a negative measurement.")
    if not generated["Expected_Potability"].isin([0, 1]).all():
        raise ValueError("Expected_Potability must contain only 0 or 1.")

    real_feature_rows = set(
        tuple(row)
        for row in cleaned_data[FEATURE_COLUMNS].round(6).itertuples(index=False, name=None)
    )
    generated_feature_rows = set(
        tuple(row)
        for row in generated[FEATURE_COLUMNS].itertuples(index=False, name=None)
    )
    copied_rows = real_feature_rows.intersection(generated_feature_rows)
    if copied_rows:
        raise ValueError("Generated scenarios must not be exact copies of real records.")


def write_report(cleaned_data, generated):
    """Write a human-readable record of the generation method and safeguards."""
    expected_counts = generated["Expected_Potability"].value_counts().sort_index()
    REPORT_FILE.write_text(
        "# SC11 Generated Testing Scenarios\n\n"
        "## Purpose\n"
        "These records are generated testing scenarios for the SC11 teaching example. "
        "They are not new laboratory measurements and are not presented as real data.\n\n"
        "## Source and size\n"
        f"- Cleaned cited real records: {len(cleaned_data):,}\n"
        f"- Generated scenario ratio: {SCENARIO_RATIO:.0%}\n"
        f"- Generated scenarios: {len(generated):,}\n"
        "- Output file: `data/generated/generated_water_quality_test_scenarios.csv`\n\n"
        "## Reproducible method\n"
        f"- Fixed random seed: `{SEED}`\n"
        "- A balanced set was sampled from the two real-data classes.\n"
        "- Every water-quality feature was adjusted with small Gaussian jitter equal to one percent of that feature's interquartile range.\n"
        "- Values were clipped to the observed cleaned-data range; pH was additionally constrained to 0-14.\n"
        "- `Expected_Potability` is inherited from the sampled source class for testing expectations only; it is not a fresh lab-verified label.\n\n"
        "## Validation performed\n"
        f"- Exactly {len(generated):,} scenario IDs were created.\n"
        "- No missing values, duplicate scenario IDs, duplicate generated feature rows, or exact copies of real feature rows are allowed.\n"
        "- All pH values and non-negative measurement checks passed.\n"
        f"- Expected labels: 0 = {expected_counts.get(0, 0)}, 1 = {expected_counts.get(1, 0)}.\n\n"
        "## Strict usage rule\n"
        "Use these scenarios only for product testing, input validation and demonstration. "
        "Do not mix them into `train.csv`, `validation.csv` or `test.csv`, and do not use them to claim model accuracy.\n",
        encoding="utf-8",
    )


def run_generator():
    """Create, validate and save the documented testing scenarios."""
    cleaned_data = pd.read_csv(INPUT_FILE)
    generated = generate_scenarios(cleaned_data)
    validate_scenarios(generated, cleaned_data)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    generated.to_csv(OUTPUT_FILE, index=False)
    write_report(cleaned_data, generated)

    print("SC11 GENERATED TESTING SCENARIOS COMPLETED")
    print("-" * 50)
    print(f"Real cleaned records: {len(cleaned_data)}")
    print(f"Generated testing scenarios: {len(generated)}")
    print(f"Generation seed: {SEED}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Report file: {REPORT_FILE}")


if __name__ == "__main__":
    run_generator()
