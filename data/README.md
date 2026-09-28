# SC11 Water Quality Potability - Data Documentation

## Project purpose
This project predicts whether a water sample is potable or not potable from its chemical and physical water-quality measurements.

## Primary labelled dataset
- Dataset: Water Potability
- Source: https://huggingface.co/datasets/Kavi-ya/Water-Potability
- Licence: MIT
- Downloaded file: water_potability_balanced.csv
- Source records: 2,556
- Target: Potability
  - 0 = Not potable
  - 1 = Potable

## Input fields
- ph
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic_carbon
- Trihalomethanes
- Turbidity

## Safety note
This is an educational decision-support project. Predictions do not replace laboratory testing or official drinking-water certification.

## Step 2 plan
1. Store the original downloaded file in data/raw/.
2. Inspect missing values, duplicates, columns, and class balance.
3. Clean and save usable data in data/processed/.
4. Create reproducible train, validation, and test splits.
5. Generate and document 10,000+ separate testing scenarios.
