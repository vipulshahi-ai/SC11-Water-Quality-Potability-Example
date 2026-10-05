"""SC11 Step 3 - train an ANN water-potability classifier.

Copy this file to src/train_ann.py after creating the step-3-ann-model branch.
Run it from VS Code using the Run Python File button.
"""

from pathlib import Path
import json
import pickle

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "data" / "reports"
MODEL_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

FEATURES = [
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
TARGET = "Potability"
RANDOM_SEED = 42


def load_split(name):
    """Load one Step 2 dataset split and verify its required columns."""
    path = DATA_DIR / f"{name}.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Cannot find {path}. Complete the Step 2 data pipeline first."
        )

    dataframe = pd.read_csv(path)
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in dataframe.columns]
    if missing:
        raise ValueError(f"{name}.csv is missing columns: {missing}")
    if dataframe[required].isna().sum().sum() != 0:
        raise ValueError(f"{name}.csv still contains missing values.")
    return dataframe


def split_xy(dataframe):
    return dataframe[FEATURES], dataframe[TARGET]


def build_ann():
    """Create a small feed-forward ANN trained through backpropagation."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "ann",
                MLPClassifier(
                    hidden_layer_sizes=(16, 8),
                    activation="relu",
                    solver="adam",
                    learning_rate_init=0.001,
                    max_iter=400,
                    early_stopping=True,
                    validation_fraction=0.15,
                    n_iter_no_change=25,
                    random_state=RANDOM_SEED,
                ),
            ),
        ]
    )


def calculate_metrics(y_true, y_pred, split_name):
    return {
        "split": split_name,
        "accuracy": round(accuracy_score(y_true, y_pred), 4),
        "precision": round(precision_score(y_true, y_pred, zero_division=0), 4),
        "recall": round(recall_score(y_true, y_pred, zero_division=0), 4),
        "f1_score": round(f1_score(y_true, y_pred, zero_division=0), 4),
    }


def save_confusion_matrix(y_true, y_pred, split_name):
    matrix = confusion_matrix(y_true, y_pred, labels=[0, 1])
    figure, axis = plt.subplots(figsize=(5, 4))
    image = axis.imshow(matrix, cmap="Blues")
    figure.colorbar(image, ax=axis)
    axis.set(
        title=f"ANN Confusion Matrix - {split_name.title()} Split",
        xlabel="Predicted label",
        ylabel="Actual label",
        xticks=[0, 1],
        yticks=[0, 1],
        xticklabels=["Not potable", "Potable"],
        yticklabels=["Not potable", "Potable"],
    )
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            axis.text(column, row, matrix[row, column], ha="center", va="center")
    figure.tight_layout()
    figure.savefig(RESULTS_DIR / f"step3_{split_name}_confusion_matrix.png", dpi=180)
    plt.close(figure)


def save_loss_curve(model):
    losses = model.named_steps["ann"].loss_curve_
    figure, axis = plt.subplots(figsize=(7, 4))
    axis.plot(range(1, len(losses) + 1), losses, marker="o", markersize=2)
    axis.set(
        title="ANN Training Loss Curve",
        xlabel="Training iteration",
        ylabel="Loss",
    )
    axis.grid(alpha=0.3)
    figure.tight_layout()
    figure.savefig(RESULTS_DIR / "step3_ann_loss_curve.png", dpi=180)
    plt.close(figure)


def save_predictions(dataframe, predictions, probabilities, split_name):
    output = dataframe.copy()
    output["ann_prediction"] = predictions
    output["ann_potable_probability"] = probabilities[:, 1]
    output.to_csv(REPORT_DIR / f"step3_{split_name}_predictions.csv", index=False)


def main():
    for directory in [REPORT_DIR, MODEL_DIR, RESULTS_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    train_data = load_split("train")
    validation_data = load_split("validation")
    test_data = load_split("test")
    x_train, y_train = split_xy(train_data)
    x_validation, y_validation = split_xy(validation_data)
    x_test, y_test = split_xy(test_data)

    print("SC11 STEP 3 - ANN TRAINING")
    print("=" * 45)
    print(f"Features: {len(FEATURES)}")
    print("Architecture: 9 inputs -> 16 -> 8 -> 1 output")
    print(f"Train rows: {len(train_data)}")
    print(f"Validation rows: {len(validation_data)}")
    print(f"Test rows: {len(test_data)}")

    model = build_ann()
    model.fit(x_train, y_train)

    metrics = []
    for split_name, dataframe, features, target in [
        ("validation", validation_data, x_validation, y_validation),
        ("test", test_data, x_test, y_test),
    ]:
        predictions = model.predict(features)
        probabilities = model.predict_proba(features)
        metrics.append(calculate_metrics(target, predictions, split_name))
        save_confusion_matrix(target, predictions, split_name)
        save_predictions(dataframe, predictions, probabilities, split_name)

        print(f"\n{split_name.title()} metrics")
        print(pd.DataFrame([metrics[-1]]).to_string(index=False))
        print(classification_report(target, predictions, zero_division=0))

    metrics_frame = pd.DataFrame(metrics)
    metrics_frame.to_csv(REPORT_DIR / "step3_ann_metrics.csv", index=False)
    save_loss_curve(model)

    with (MODEL_DIR / "ann_water_potability.pkl").open("wb") as model_file:
        pickle.dump(model, model_file)
    metadata = {
        "project": "SC11 Water Quality Potability",
        "technique": "Feed-forward ANN / backpropagation",
        "features": FEATURES,
        "target": TARGET,
        "random_seed": RANDOM_SEED,
        "architecture": "9 inputs -> 16 -> 8 -> 1 output",
    }
    (MODEL_DIR / "ann_model_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )

    print("\nSaved model:", MODEL_DIR / "ann_water_potability.pkl")
    print("Saved metrics:", REPORT_DIR / "step3_ann_metrics.csv")
    print("Saved figures:", RESULTS_DIR)
    print("\nSTEP 3 COMPLETED")


if __name__ == "__main__":
    main()
