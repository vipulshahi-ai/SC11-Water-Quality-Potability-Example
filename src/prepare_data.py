from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "water_potability_balanced.csv"


def inspect_data():
    df = pd.read_csv(RAW_FILE)

    print("SC11 WATER QUALITY DATA INSPECTION")
    print("-" * 45)

    print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print(f"\nDuplicate rows: {df.duplicated().sum()}")

    print("\nPotability class distribution:")
    print(df["Potability"].value_counts().sort_index())

    print("\nFirst five rows:")
    print(df.head())


if __name__ == "__main__":
    inspect_data()