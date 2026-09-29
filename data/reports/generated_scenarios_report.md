# SC11 Generated Testing Scenarios

## Purpose
These records are generated testing scenarios for the SC11 teaching example. They are not new laboratory measurements and are not presented as real data.

## Source and size
- Cleaned cited real records: 2,556
- Generated scenario ratio: 10%
- Generated scenarios: 256
- Output file: `data/generated/generated_water_quality_test_scenarios.csv`

## Reproducible method
- Fixed random seed: `42`
- A balanced set was sampled from the two real-data classes.
- Every water-quality feature was adjusted with small Gaussian jitter equal to one percent of that feature's interquartile range.
- Values were clipped to the observed cleaned-data range; pH was additionally constrained to 0-14.
- `Expected_Potability` is inherited from the sampled source class for testing expectations only; it is not a fresh lab-verified label.

## Validation performed
- Exactly 256 scenario IDs were created.
- No missing values, duplicate scenario IDs, duplicate generated feature rows, or exact copies of real feature rows are allowed.
- All pH values and non-negative measurement checks passed.
- Expected labels: 0 = 128, 1 = 128.

## Strict usage rule
Use these scenarios only for product testing, input validation and demonstration. Do not mix them into `train.csv`, `validation.csv` or `test.csv`, and do not use them to claim model accuracy.
