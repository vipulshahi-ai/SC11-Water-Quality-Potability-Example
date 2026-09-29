# SC11 Data Quality Report

## Purpose
This report records how the Water Quality Potability dataset was inspected, cleaned, validated, and split for the SC11 project.

## Dataset source
- Dataset: Water Potability
- Source: https://huggingface.co/datasets/Kavi-ya/Water-Potability
- Licence: MIT
- Original file: `data/raw/water_potability_balanced.csv`
- Original records: 2,556
- Target column: `Potability`
  - `0` = Not potable
  - `1` = Potable

## Raw-data inspection

| Check | Result |
|---|---:|
| Rows | 2,556 |
| Columns | 10 |
| Missing values in `ph` | 372 |
| Missing values in `Sulfate` | 609 |
| Missing values in `Trihalomethanes` | 129 |
| Total missing values | 1,110 |
| Duplicate rows | 0 |
| Not-potable records | 1,278 |
| Potable records | 1,278 |

## Cleaning method
- The original raw CSV was not modified.
- Missing numeric values were filled using the median of their own column.
- Exact duplicate rows were removed if present.
- The cleaned dataset was checked for missing values, duplicate rows, invalid pH values, negative measurements, and invalid target labels.

## Validation result
All validation checks passed after cleaning:

- No required columns were missing.
- No missing values remained.
- All pH values were between 0 and 14.
- No negative water-quality measurements were found.
- `Potability` contained only `0` and `1`.
- No duplicate rows remained.

## Reproducible split

A fixed random seed of `42` was used. The data was split separately for each Potability class to preserve the balanced class distribution.

| Dataset | Rows | Purpose |
|---|---:|---|
| `train.csv` | 1,788 | Model training |
| `validation.csv` | 384 | Model selection and tuning |
| `test.csv` | 384 | Final unseen evaluation |
| Total | 2,556 | Complete cleaned dataset |

## Output files

The pipeline created these files in `data/processed/`:

- `water_potability_clean.csv`
- `train.csv`
- `validation.csv`
- `test.csv`

## Limitation and generated test scenarios
The cited labelled dataset contains 2,556 real records. It must not be duplicated and described as new real observations.

For this SC11 teaching example, Step 2 also creates 256 generated water-quality testing scenarios. This is 10% of the 2,556 cited real records, rounded up. These scenarios are clearly labelled as generated test scenarios, not original laboratory observations.

The generator uses a fixed seed, applies small documented changes to sampled real-data patterns, validates the output, and saves it separately in `data/generated/`. It must never be mixed into `train.csv`, `validation.csv`, or `test.csv` and must not be used to claim model accuracy.

## Safety note
This is an educational decision-support project. Its prediction does not replace laboratory testing or official drinking-water certification.
