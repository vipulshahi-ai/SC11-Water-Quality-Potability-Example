# Step 6 - Testing and validation

## Project and environment

- Project: SC11 Water Quality Potability Example (instructor reference).
- Branch: `step-6-testing`.
- Commit tested: `e483875`.
- Python version: `3.12.1` (project `.venv`).
- Launch from the repository root: `python -m streamlit run app.py`.
- Reference input: first data row in `data/processed/validation.csv`.

## Planned tests and results

PASS means the app or script behaved as expected. An error message can be a PASS when the test is checking whether the app rejects invalid input.

| ID | Input or action | Expected behaviour | Actual result | Status |
| --- | --- | --- | --- | --- |
| T01 | Load the existing sample and run the prediction. | Show a class, a label, an educational notice and a CSV download option. | Showed class 1, `Predicted potable class`, and the educational notice. The CSV downloaded successfully. | PASS |
| T02 | Reload the sample and set pH to `0`. | Accept the lower limit and return a prediction. | Accepted pH `0` and returned class 1. | PASS |
| T03 | Reload the sample and set pH to `14`. | Accept the upper limit and return a prediction. | Accepted pH `14` and returned class 0. | PASS |
| T04 | Set pH to `15` and submit the form. | Explain the allowed range and show no prediction. | Displayed `ph: use a value from 0 to 14.` No prediction was shown. | PASS |
| T05 | Enter `one` in the pH field and submit the form. | Ask for a number and show no prediction. | Displayed `ph: enter a number.` No prediction was shown. | PASS |
| T06 | Leave Trihalomethanes blank. Keep the other inputs valid, including pH `14`. | Name the missing field and show no prediction. | Displayed `Trihalomethanes: enter a value.` No prediction was shown. | PASS |
| T07 | Rename the saved model in a temporary copy and start that copy on port `8502`. | Explain that the model or metadata is missing and hide the prediction form. | The browser showed `Saved model or metadata is missing. Restore your Step 3 files.` The prediction form was unavailable. | PASS |
| T08 | Restore the model filename, restart the copy and predict using the existing sample. | Show the form again and return a prediction for the same sample. | The form returned and showed `Predicted potable class` and `Model class: 1`. | PASS |
| T09 | Run `python src/compare_step6_predictions.py` to compare the browser and Python CSVs. | All nine measurements, the predicted class and the displayed label should match. | The script reported `PASS`. All nine measurements matched. Both results showed class 1 and `Predicted potable class`. | PASS |
| T10 | Run `python -m unittest -v test_product_predict`. | All five input validation tests should pass. | All five tests showed `ok`. The terminal reported `Ran 5 tests` and ended with `OK`. | PASS |

## Evidence

| Test IDs | Evidence |
| --- | --- |
| T01 | Browser download saved as `data/reports/step6_ui_prediction.csv`. |
| T02–T03 | Browser results: pH `0` returned class 1; pH `14` returned class 0. |
| T04–T06 | The browser showed a specific validation message for each invalid input and withheld the prediction. |
| T07–T08 | The browser on port `8502` first showed the missing-model warning. After restoring the model, the same sample returned class 1. |
| T09 | `src/compare_step6_predictions.py` compared `data/reports/step6_ui_prediction.csv` with `data/reports/step5_ui_reference_prediction.csv`. The script reported `PASS`. |
| T10 | `test_product_predict.py`: five named tests showed `ok`, followed by `Ran 5 tests` and `OK`. |

## Failures, fixes and retests

- The first CSV comparison attempt could not run because `src/compare_step6_predictions.py` was missing. After adding the script, I reran the command. All nine inputs, the class and the label matched.
- The missing-model warning in T07 was intentional. The test used a temporary copy. After restoring the original model filename and restarting the copy, the normal prediction worked again in T08.
- No app defects were observed in the cases recorded above.

## Known limits

- The CSV comparison used one validation sample. It shows that the browser and Python script agree for that sample.
- The automated tests check input validation. The browser tests check the app behaviour shown in the table.
- SC11 is an educational example. Its predictions cannot certify that water is safe to drink.

## Contributions

- Instructor example: ran the browser checks, tested model recovery, compared the two CSVs, ran the automated tests and recorded the results.