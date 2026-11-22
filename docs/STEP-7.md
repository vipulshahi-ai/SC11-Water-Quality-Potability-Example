# Step 7 - Final documentation and demonstration preparation

## Project and version
- Project: SC11 Water Quality Potability Example.
- Purpose: instructor worked example for all Soft Computing project teams.
- Branch: step-7-final-documentation.
- Tested base: the completed step-6-testing branch.
- Base commit: be32e84. The final Step 7 commit is visible in Git history after publication.

## Feedback and remaining work
SC11 is an instructor example. This is a technical review list, not invented faculty feedback or a student grade.

| Check or gap | Action and evidence | Status |
| --- | --- | --- |
| README still described Step 5 | Added project overview, current commands, environment, report and slide paths. | Done |
| CSV comparison script was previously missing | Existing script rerun. All nine inputs, class and label match. See step7_csv_comparison.txt. | PASS on one saved sample |
| Input validation needs a recorded check | Five existing unittest methods rerun. See step7_validation_tests.txt. | PASS for these tests |
| Missing values were filled before splitting | Record preprocessing leakage in the report. Future improvement: split first and fit imputation on training rows only, then retrain and reevaluate. | Open limitation |
| Fresh-install reproducibility | Record a separate clean-environment check rather than assuming the working .venv proves installation works. | PASS: separate environment; see step7_fresh_check.txt. Published-clone check remains separate. |
| Presentation and PDF exports | Prepared matching eight-slide PPTX and PDF; slide renders and package checks passed. | Files prepared |
| Faculty feedback and live student assessment | Record only if actually received or performed. | Not applicable to this instructor reference |

## Final deliverables
- report/final_report.md and its checked PDF export.
- presentation/project_presentation.pptx: editable deck for the demonstration and portal upload.
- presentation/project_presentation.pdf: matching reading copy.
- Maximum 8 slides in total, including title, hidden and appendix slides; .pptx upload at most 10 MB.
- README.md with the actual install and run commands.
- Existing code, saved model, metadata and Step 4/6 evidence required to run the example.

## Demonstration rehearsal
| Case | Action | Expected behaviour | Rehearsal observation |
| --- | --- | --- | --- |
| Normal | Load the existing validation sample and predict | Class 1 and educational notice; CSV download | Class 1 and notice displayed. New download not verified: browser stalled. |
| Upper boundary | Reload sample and set pH to 14 | Accept input and return a prediction | pH 14 accepted; class 0 displayed. |
| Invalid | Reload sample and set pH to 15 | Range error; no prediction | pH 15 range error displayed; no prediction. |
| Missing model | Use the separate-copy procedure from Step 6 | Explain missing file and withhold form | Not repeated here. Historical Step 6 evidence remains separate. |

## What the results mean
On the saved 384-row test split, baseline accuracy is 0.5000 and ANN accuracy is 0.6276. ANN precision is 0.6310, recall is 0.6146 and F1 is 0.6227 for positive class Potability=1. The ANN improves on this simple baseline on this split. This does not prove real-world reliability.

## Preparation status
- Documentation: report and README prepared against the current Step 6 files. PDF and presentation checks are recorded when completed.
- Rehearsal: three browser cases observed on 22 November 2026; see the table above. Fresh CSV download remains unchecked.
- Faculty review: record actual feedback when received.
- Open limits: preprocessing before the split, small evaluation splits, one-row UI parity check and no real-world water certification.

## Contributions
SC11 is an instructor example. Student teams must name each actual member and record their specific report, testing, presentation or implementation work.

## Separate environment check
Python 3.12.1, installation from requirements-step7-runtime.txt, pip check, five validator tests and existing saved-CSV parity passed in a separate project copy. Evidence: data/reports/step7_fresh_check.txt. This does not yet prove a fresh published clone works.
