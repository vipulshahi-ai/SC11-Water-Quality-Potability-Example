# SC11 - Water Quality Potability Example
# Final Project Report

## 1. Project and author
SC11 is an instructor teaching example for the Soft Computing capstone workflow. Student teams replace the project identity and describe their own actual work.

## 2. Problem and intended user
The example accepts nine water-quality measurements and returns an ANN prediction of the dataset's potability class. It demonstrates a saved-model decision-support interface. It is not a laboratory water-quality certification tool.

## 3. Inputs and output
Inputs: ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes and Turbidity. The interface displays pH as unitless; Hardness and Sulfate in mg/L; Solids, Chloramines and Organic_carbon in ppm; Conductivity in microsiemens/cm; Trihalomethanes in micrograms/L; and Turbidity in NTU. These units require confirmation against the original dataset documentation before real use. Output: Potability class 0 or 1, a readable label and an educational-use notice.

## 4. Data and preparation
The saved Step 4 comparison evaluates 384 validation rows and 384 test rows. Keep the original Step 2 split fixed during this comparison. The project records the source as https://huggingface.co/datasets/Kavi-ya/Water-Potability, filename water_potability_balanced.csv, 2,556 records and MIT licence in data/README.md. This source/licence statement comes from the repository record. The source file contains 1,278 records in each class. Training uses 1,788 rows. The separate generated file contains 256 scenarios and is not part of model scoring. The existing preparation fills missing values using full-dataset column medians before creating the splits. This lets held-out data influence preprocessing. The reported scores must therefore be read with that limitation. A stricter future pipeline should split first and fit imputation only on the training rows, then apply it to validation/test rows and retrain the model. Generated scenarios are separate from observed labelled records.

## 5. Method
The Step 3 model is a feed-forward ANN with nine inputs and hidden layers of 16 and 8 units. The saved artifact contains the fitted pipeline used by the app. Its metadata records the feature order and random seed 42. No retraining occurs in the interface.

## 6. Simple baseline
The baseline selects the more common training label and predicts it for every held-out row. A training tie is resolved as class 0. The rule is chosen from training labels only. Both methods are scored on identical held-out records.

## 7. Saved comparison results
| Split | Method | Rows | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- | --- | --- |
| Validation | Majority baseline | 384 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| Validation | ANN | 384 | 0.5443 | 0.5415 | 0.5781 | 0.5592 |
| Test | Majority baseline | 384 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| Test | ANN | 384 | 0.6276 | 0.6310 | 0.6146 | 0.6227 |

Precision, recall and F1 treat Potability=1 as the positive class.
Source: data/reports/step4_baseline_metrics.csv.
Differences: data/reports/step4_comparison.csv.
Figure: results/step4_baseline_vs_ann.png.

## 8. Interpretation
Test accuracy rises from 50.00% to 62.76%, an increase of 12.76 percentage points. Validation accuracy rises by 4.43 percentage points. The always-zero baseline misses every class-1 case, so its positive-class recall is zero. ANN recall is 61.46% on the test split, which still leaves errors. The results show improvement over this baseline on these records, not proof of reliable use on unseen real-world water samples.

## 9. Interface and reproducibility
Entry file: app.py. Inference code: src/product_predict.py.
Install in the project's recorded environment:
python -m pip install -r requirements-step7-runtime.txt
Launch:
python -m streamlit run app.py
Load the existing validation example, predict and save the CSV output.
Verified working environment on 22 November 2026: Python 3.12.1; pandas 3.0.6, numpy 2.5.3, scikit-learn 1.9.1, scipy 1.18.1, matplotlib 3.11.2, streamlit 1.66.1. requirements-step7-runtime.txt records these direct runtime versions. A separate project copy was installed in a new environment on 22 November 2026. pip check, five validator tests and the existing saved-CSV comparison passed. See data/reports/step7_fresh_check.txt. A fresh published clone has not yet been checked.

## 10. Testing evidence
docs/STEP-6.md records ten cases: normal, lower and upper pH boundaries, out-of-range pH, text in a numeric field, missing input, missing model, recovery, CSV comparison and unit tests.
The saved normal sample gives class 1. pH 0 gives class 1; pH 14 gives class 0. pH 15 is rejected. These are observations from the recorded reference run.
The five existing validation unit tests were rerun on 22 November 2026 and passed. The saved CSV comparison was also rerun and passed. See data/reports/step7_validation_tests.txt and step7_csv_comparison.txt. The browser CSV and Python reference matched on nine measurements, class and label for one sample.

## 11. Faults, fixes and limits
The comparison script was initially missing. After it was added, the parity check passed. A missing-model warning was deliberately tested in a temporary copy; restoring the file allowed prediction again.
Full-dataset median filling before the split can make held-out results optimistic. The balanced source also differs from real-world prevalence. The unit tests check validation and do not establish model accuracy. One matching CSV row does not establish consistency for every possible input. Model quality is limited to the available dataset and evaluation design.

## 12. Demonstration
The 22 November rehearsal on the separately installed app displayed class 1 for the normal example, accepted pH 14 with class 0, and rejected pH 15 with a range message and no prediction. A new browser CSV download stalled and remains unchecked. The existing saved-CSV comparison passed; it is not evidence of a new download. The missing-model case was recorded in Step 6 and was not repeated. These are technical rehearsal observations, not a formal faculty assessment.

## 13. Contributions
SC11 is an instructor example. Student teams record each actual member's specific work, evidence and demonstration role here.

## 14. Conclusion and next work
The example connects a saved ANN to a validated input form and compares it with a training-majority baseline. Further work includes broader app/reference testing, stronger independent evaluation, dependency reproducibility and domain review before any real-world use.

## 15. References and evidence index
- Dataset record: data/README.md and data/reports/data_quality_report.md, which cite https://huggingface.co/datasets/Kavi-ya/Water-Potability and MIT. Confirm original redistribution terms before reuse.
- Method and model: docs/STEP-3.md, src/train_ann.py and models/.
- Baseline: docs/STEP-4.md and src/compare_baseline.py.
- Evaluation: data/reports/step4_baseline_metrics.csv.
- Interface and tests: app.py, src/product_predict.py, docs/STEP-6.md.
- Final presentation: presentation/project_presentation.pdf after export.
