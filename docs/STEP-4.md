# SC11 Step 4 - Fair baseline comparison

## Question
On the same held-out validation and test rows, does the Step 3 ANN predict
potability better than a simple training-majority baseline?

## Baseline rule
Count `Potability` labels in `data/processed/train.csv` only. Always predict
the more common label. If tied, choose `0`. Never look at validation/test labels
while choosing this rule.

## Fairness checks
- Step 3 ANN predictions come from `step3_validation_predictions.csv` and
  `step3_test_predictions.csv`.
- `src/compare_baseline.py` checks row count, feature columns and true labels
  against the same Step 2 validation/test CSVs before scoring.
- The held-out test set is not used to tune either method.
- Generated Step 2 scenarios are kept separate; they are not real labelled
  observations and are not included in this comparison.

## Results

These are the saved results from `data/reports/step4_baseline_metrics.csv`. Precision,
recall and F1 treat `Potability = 1` as the positive class.

| Split | Method | Rows | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|
| Validation | Majority baseline | 384 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| Validation | Step 3 ANN | 384 | 0.5443 | 0.5415 | 0.5781 | 0.5592 |
| Test | Majority baseline | 384 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| Test | Step 3 ANN | 384 | 0.6276 | 0.6310 | 0.6146 | 0.6227 |

## Interpretation
- The training split has 894 records of each class. Because it is tied, the
  documented baseline predicts `0` for every record. It never predicts a
  potable case, so its precision, recall and F1 for class `1` are zero.
- On validation, ANN accuracy is 0.5443 versus 0.5000 for the baseline: an
  increase of **0.0443 score points**. Validation F1 is 0.5592 versus 0.0000.
- On test, ANN accuracy is 0.6276 versus 0.5000: an increase of **0.1276 score
  points**. Test F1 is 0.6227 versus 0.0000. See
  `data/reports/step4_comparison.csv` for all four metric differences.
- The ANN is higher on every metric reported here; no measured metric became
  worse in this comparison. This does not establish that it is reliable for
  drinking-water decisions.
- The balanced class distribution makes the always-`0` baseline's accuracy
  0.5000, yet that same rule misses every class-`1` case. Accuracy alone hides
  this failure; precision, recall and F1 must be read alongside it.
- The cited labelled dataset has only 2,556 records, and some source values
  were missing and filled during Step 2. The 256 generated scenarios are not
  independent laboratory labels and are excluded from these scores. This
  comparison is limited to the available held-out data and one simple baseline.

## Evidence
- `src/compare_baseline.py`
- `notebooks/03_baseline_comparison.ipynb` executed with visible outputs
- `data/reports/step4_baseline_metrics.csv`
- `data/reports/step4_comparison.csv`
- `data/reports/step4_validation_paired_predictions.csv`
- `data/reports/step4_test_paired_predictions.csv`
- `results/step4_baseline_vs_ann.png`

## Safety and scope
This is an educational model comparison. Neither method can establish that
water is safe to drink. Laboratory analysis and the relevant official
standards are still required for any real-world decision. Step 4 is a fair
comparison, not the final Product V1 interface.

## Team contributions
SC11 is an instructor teaching example, not an allocated student team. There
are no student member contributions to claim here. Each allocated team must
replace this section with its real members' names and specific work before
submitting its own Step 4 report.
