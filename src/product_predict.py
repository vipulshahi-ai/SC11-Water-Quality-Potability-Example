"""SC11 Product V1 inference. Adapt the schema for your own project."""
from pathlib import Path
import json
import math
import pickle

FEATURES = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity",
    ]

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "ann_water_potability.pkl"
META_PATH = ROOT / "models" / "ann_model_metadata.json"

def validate_inputs(values):
    """Reject blank, nonnumeric, nonfinite and physically invalid values."""
    clean = {}
    for name in FEATURES:
        raw = values.get(name)
        if raw is None or str(raw).strip() == "":
            raise ValueError(f"{name}: enter a value.")
        try:
            number = float(raw)
        except (ValueError, TypeError) as error:
            raise ValueError(f"{name}: enter a number.") from error
        if not math.isfinite(number):
            raise ValueError(f"{name}: use a finite number.")
        if name == "ph" and not 0 <= number <= 14:
            raise ValueError("ph: use a value from 0 to 14.")
        if name != "ph" and number < 0:
            raise ValueError(f"{name}: negative values are invalid.")
        clean[name] = number
    return clean

def load_model():
    """Load only the model you created and trust in this repository."""
    if not MODEL_PATH.is_file() or not META_PATH.is_file():
        raise FileNotFoundError(
            "Saved model or metadata is missing. Restore your Step 3 files."
        )
    metadata = json.loads(META_PATH.read_text(encoding="utf-8"))

    if metadata.get("features") != FEATURES:
        raise ValueError("Model metadata feature order does not match the app.")
    with MODEL_PATH.open("rb") as source:
        model = pickle.load(source)
    if list(getattr(model, "feature_names_in_", [])) != FEATURES:
        raise ValueError("Saved model input columns do not match the app.")
    return model

def predict_one(model, values):
    import pandas as pd

    clean = validate_inputs(values)
    frame = pd.DataFrame([[clean[name] for name in FEATURES]], columns=FEATURES)
    prediction = int(model.predict(frame)[0])
    if prediction not in (0, 1):
        raise ValueError("Unexpected model class. Check the saved model.")
    return {
        "predicted_class": prediction,
        "label": "Predicted potable class" if prediction == 1
        else "Predicted non-potable class",
        "notice": "Educational prediction only. This does not certify drinking-water safety.",
        **clean,
        }