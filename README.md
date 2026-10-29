# Step 5 - Product V1

## 1. Project details

- Project code: SC11
- Project title: Water Quality Potability Example
- Purpose: Instructor reference for Soft Computing capstone projects
- Branch: `step-5-product-v1`
- Application framework: Streamlit
- Python version used: 3.12.1

SC11 is an instructor example. Student teams should use this report
as a reference and document the actual work completed for their own
allocated projects.

## 2. What is Product V1?

Product V1 is the first working version of an application that a user
can operate.

In this example, the application allows a user to enter water-quality
measurements. It checks the inputs and uses the ANN model created in
Step 3 to return a predicted class.

The application is an educational demonstration. It does not certify
whether water is safe to drink.

## 3. User task

A learner or reviewer can use the application to understand how a
trained model receives inputs and produces a prediction.

The user enters nine measurements:

| Input | Unit shown in the interface |
|---|---|
| pH | Unitless |
| Hardness | mg/L |
| Solids | ppm |
| Chloramines | ppm |
| Sulfate | mg/L |
| Conductivity | microsiemens/cm |
| Organic carbon | ppm |
| Trihalomethanes | micrograms/L |
| Turbidity | NTU |

The units shown in the interface should be checked against the source
dataset documentation before any real-world use.

## 4. How the application works

1. The user enters nine water measurements in the interface.
2. The application checks the inputs for missing or invalid values.
3. If the inputs are valid, the application uses the saved ANN model
   from Step 3.
4. The model returns a predicted class.
5. The application displays the class, a readable label and an
   educational-use notice.
6. The user can download the result as a CSV file.

The application uses the model for prediction. It does not train the
model again when the user clicks the prediction button.

The saved model has the following architecture:

`9 inputs -> 16 hidden units -> 8 hidden units -> 1 output`

## 5. Main project files

| File | Purpose |
|---|---|
| `app.py` | Creates the Streamlit user interface |
| `src/product_predict.py` | Checks inputs and uses the saved model |
| `models/ann_water_potability.pkl` | Saved ANN model |
| `models/ann_model_metadata.json` | Records the model's expected features |
| `requirements-product-v1.txt` | Lists the Product V1 dependencies |
| `test_product_predict.py` | Contains automated input-validation tests |
| `src/check_product_prediction.py` | Generates a reference prediction |
| `data/reports/step5_ui_reference_prediction.csv` | Stores the reference prediction |
| `docs/STEP-5.md` | Explains the application and the recorded tests |

## 6. How to run the application

Open a terminal in the project folder and select the Python environment
used for the earlier project work.

Install the required packages:

```bash
python -m pip install -r requirements-product-v1.txt
```

Start the application:

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal. In this example, it
was:

```text
http://localhost:8501
```

Keep the terminal running while using the application. Press `Ctrl+C`
in the terminal to stop it.

## 7. Tests and observations

The purpose of testing is to compare the expected behaviour with the
behaviour actually observed.

| Test | Expected behaviour | Observation | Result |
|---|---|---|---|
| Normal input | Valid inputs are accepted and a prediction is displayed. | The existing example produced class `1`, labelled “Predicted potable class”. | Pass |
| pH boundary in interface | pH `14` is accepted by the input validation. | The application returned class `0`, labelled “Predicted non-potable class”. This is a boundary test, not a drinking-water recommendation. | Pass |
| Missing input in interface | A missing value is rejected with a clear message. | A blank Trihalomethanes field produced: “Trihalomethanes: enter a value.” | Pass |
| Reference script and interface | The same inputs and saved model produce the same predicted class. | Both the reference CSV and interface showed class `1` for the existing example. | Pass |
| Result download | The result can be downloaded as a CSV file. | The downloaded CSV showed class `1`, the predicted label, notice and input values. | Pass |
| Automated validation tests | All five test methods pass. | Five tests completed with `ok`; the final result was `OK`. | Pass |
| Missing model | A useful error should be displayed when the model is unavailable. | This test has not yet been verified in a temporary project copy. | Not yet tested |

### Reference example

The reference prediction used these input values:

| Input | Value |
|---|---:|
| pH | 4.941972156828116 |
| Hardness | 166.71044045521649 |
| Solids | 19806.411303229328 |
| Chloramines | 8.031864862891307 |
| Sulfate | 426.1575185722385 |
| Conductivity | 352.0390921282106 |
| Organic carbon | 15.496886933983603 |
| Trihalomethanes | 68.60840186648572 |
| Turbidity | 5.076146746327639 |

For this example, both the reference prediction and the interface
displayed:

- Predicted class: `1`
- Displayed label: “Predicted potable class”

This label is a model prediction. It does not establish that the water
is safe to drink.

## 8. Automated checks with unittest

`unittest` is a tool included with Python for running automated tests.

A unit test checks a small part of a program. It compares the observed
behaviour with the behaviour expected by the test.

For this project, the five test methods check:

1. A normal input.
2. The pH boundaries of `0` and `14`.
3. Invalid pH values.
4. A negative turbidity value.
5. A missing Hardness input.

Run the tests from the project root:

```bash
python -m unittest test_product_predict -v
```

Observed result:

```text
Ran 5 tests

OK
```

Each test was shown with `ok` before the final result. For an invalid
input, a passing test means that the program raised the expected
validation error.

These tests check selected input-validation behaviour. They do not
prove that the model is accurate or that every interface action works.

## 9. Evidence

The project contains the following evidence files:

- [Reference prediction CSV](../data/reports/step5_ui_reference_prediction.csv)
- [Reference prediction script](../src/check_product_prediction.py)
- [Input-validation test file](../test_product_predict.py)
- [Application code](../app.py)
- [Prediction and validation code](../src/product_predict.py)

Screenshots used in the teaching guide show the application, the
prediction result, the missing-input message and the automated test
output.

## 10. Earlier feedback

SC11 is an instructor teaching example rather than an allocated
student team's submission.

Student teams should use this section to record relevant feedback from
earlier steps, explain the corrections they made and link to the
related files or commits.

## 11. Limitations and responsible use

- This application is an educational demonstration.
- A model prediction does not certify drinking-water safety.
- Input validation does not guarantee that an accepted value is
  representative of the model's training data.
- The automated tests cover selected input-validation behaviour.
- Passing these tests does not establish the accuracy of the ANN.
- Real drinking-water decisions require appropriate laboratory
  analysis and relevant official standards.

## 12. Contributions

SC11 is an instructor teaching example, not an allocated student team.

Each student team should replace this section with its actual members,
their individual contributions and the related evidence.