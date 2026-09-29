from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "water_potability_balanced.csv"
)

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

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

REQUIRED_COLUMNS = FEATURE_COLUMNS + ["Potability"]

SEED = 42
VALIDATION_RATIO = 0.15
TEST_RATIO = 0.15


def clean_data(dataframe):
    """Fill missing values and remove duplicate rows."""
    cleaned = dataframe.copy()

    cleaned[FEATURE_COLUMNS] = cleaned[FEATURE_COLUMNS].fillna(
        cleaned[FEATURE_COLUMNS].median()
    )

    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    return cleaned


def validate_data(dataframe):
    """Validate cleaned data before creating model splits."""
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if dataframe[REQUIRED_COLUMNS].isna().sum().sum() != 0:
        raise ValueError("Missing values are still present after cleaning.")

    if not dataframe["ph"].between(0, 14).all():
        raise ValueError("Some pH values are outside the valid range 0 to 14.")

    if (dataframe[FEATURE_COLUMNS] < 0).sum().sum() != 0:
        raise ValueError("Negative values found in water-quality measurements.")

    if not dataframe["Potability"].isin([0, 1]).all():
        raise ValueError("Potability must contain only 0 or 1.")

    if dataframe.duplicated().sum() != 0:
        raise ValueError("Duplicate rows remain after cleaning.")


def create_stratified_splits(dataframe):
    """Create balanced train, validation and test datasets."""
    train_parts = []
    validation_parts = []
    test_parts = []

    for label, group in dataframe.groupby("Potability", sort=True):
        shuffled_group = group.sample(
            frac=1,
            random_state=SEED + int(label)
        ).reset_index(drop=True)

        total_rows = len(shuffled_group)
        test_rows = round(total_rows * TEST_RATIO)
        validation_rows = round(total_rows * VALIDATION_RATIO)

        test_parts.append(shuffled_group.iloc[:test_rows])
        validation_parts.append(
            shuffled_group.iloc[test_rows:test_rows + validation_rows]
        )
        train_parts.append(
            shuffled_group.iloc[test_rows + validation_rows:]
        )

    train_data = pd.concat(train_parts).sample(
        frac=1,
        random_state=SEED
    ).reset_index(drop=True)

    validation_data = pd.concat(validation_parts).sample(
        frac=1,
        random_state=SEED
    ).reset_index(drop=True)

    test_data = pd.concat(test_parts).sample(
        frac=1,
        random_state=SEED
    ).reset_index(drop=True)

    return train_data, validation_data, test_data


def run_pipeline():
    """Run the complete Step 2 SC11 data pipeline."""
    raw_data = pd.read_csv(RAW_FILE)

    duplicate_rows_before = int(raw_data.duplicated().sum())
    missing_values_before = int(raw_data.isna().sum().sum())

    cleaned_data = clean_data(raw_data)
    validate_data(cleaned_data)

    train_data, validation_data, test_data = create_stratified_splits(
        cleaned_data
    )

    if len(train_data) + len(validation_data) + len(test_data) != len(cleaned_data):
        raise ValueError("Split sizes do not match the cleaned dataset size.")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    cleaned_data.to_csv(
        PROCESSED_DIR / "water_potability_clean.csv",
        index=False,
    )
    train_data.to_csv(PROCESSED_DIR / "train.csv", index=False)
    validation_data.to_csv(PROCESSED_DIR / "validation.csv", index=False)
    test_data.to_csv(PROCESSED_DIR / "test.csv", index=False)

    print("SC11 STEP 2 DATA PIPELINE COMPLETED")
    print("-" * 50)
    print(f"Raw rows: {len(raw_data)}")
    print(f"Missing values before cleaning: {missing_values_before}")
    print(f"Duplicate rows before cleaning: {duplicate_rows_before}")
    print(f"Cleaned rows: {len(cleaned_data)}")
    print(f"Training rows: {len(train_data)}")
    print(f"Validation rows: {len(validation_data)}")
    print(f"Test rows: {len(test_data)}")
    print(f"Random seed: {SEED}")
    print("\nOutput location:")
    print(PROCESSED_DIR)


if __name__ == "__main__":
    run_pipeline()