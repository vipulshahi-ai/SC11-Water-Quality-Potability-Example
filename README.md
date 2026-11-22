# SC11 - Water Quality Potability Example

An instructor reference for the Soft Computing capstone workflow at Galgotias University.
Students use the process as a guide and implement their own allocated project.

## Current work
- Step 7 branch: `step-7-final-documentation`, based on completed Step 6 commit `be32e84`.
- Final report: [Markdown](report/final_report.md) and [PDF](report/final_report.pdf).
- Presentation: [PPTX](presentation/project_presentation.pptx) and [matching PDF](presentation/project_presentation.pdf), maximum eight slides.
- Milestone record: [docs/STEP-7.md](docs/STEP-7.md).

## What the application does
Enter nine water measurements, validate the inputs and obtain a class from the saved ANN pipeline.
The interface displays a label and notice and offers a CSV download. It does not retrain the model.
This educational prediction does not certify drinking-water safety.

## Quick start on Windows
Open the project root in VS Code. Use Python 3.12.1 and the recorded model-compatible environment.
For a new clone, choose the branch containing the report and saved model.

```text
git clone --branch step-7-final-documentation https://github.com/vipulshahi-ai/SC11-Water-Quality-Potability-Example.git
cd SC11-Water-Quality-Potability-Example
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements-step7-runtime.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit, normally http://localhost:8501.
Keep that process running while using the app. Ctrl+C stops the server.
If you already have the working Step 6 environment, activate it rather than replacing it.
The recorded direct versions are pandas 3.0.6, numpy 2.5.3, scikit-learn 1.9.1, scipy 1.18.1, matplotlib 3.11.2, streamlit 1.66.1.
The fresh-install outcome, including any installation failure, is recorded separately in the Step 7 milestone record.

## First example and expected output
1. Select **Load one existing example**.
2. Select **Predict using saved ANN**.
3. The recorded sample produces class `1`, **Predicted potable class**, and the educational notice.
4. Select **Download this result as CSV** and save the CSV in `data/reports/` if comparing it with the Python reference.
5. Reload the sample, change pH to `15` and predict. Expected error: `ph: use a value from 0 to 14.` No prediction should appear.

## Checks
```text
python -m unittest -v test_product_predict
python src/compare_step6_predictions.py
```
The recorded checks return five passing validation tests and a CSV match for one saved sample.
Logs: [validation](data/reports/step7_validation_tests.txt), [CSV comparison](data/reports/step7_csv_comparison.txt), [environment](data/reports/step7_environment.json).

## Model and saved results
- Model: `models/ann_water_potability.pkl`.
- Metadata and feature order: `models/ann_model_metadata.json`.
- Architecture: nine inputs, hidden layers of 16 and 8, binary output.
- Same 384 test rows: baseline accuracy 50.00%, ANN accuracy 62.76%, ANN recall 61.46% for positive class 1.
- [Metrics](data/reports/step4_baseline_metrics.csv) and [chart](results/step4_baseline_vs_ann.png).

## Limits that affect interpretation
- The existing pipeline fills missing values before splitting. Improve this by fitting imputation on training rows only, then retrain and reevaluate.
- The balanced, 2,556-row source and 384-row test split limit generalisation.
- Generated scenarios are testing aids, not additional laboratory labels.
- Five validation tests and one matching CSV row do not establish model accuracy or complete UI coverage.
- Real water decisions need appropriate laboratory analysis and domain standards.

## Evidence and authorship
See [Step 6](docs/STEP-6.md), [Step 7](docs/STEP-7.md), [data record](data/README.md) and [report](report/final_report.md).
SC11 is an instructor example. It has no allocated student team or invented member contributions.

Separate environment check (22 November 2026): install, pip check, five validator tests and saved-CSV comparison passed. Normal/pH14/pH15 browser cases behaved as expected. A new browser CSV download and a published-clone rehearsal remain unchecked. See [check record](data/reports/step7_fresh_check.txt).
