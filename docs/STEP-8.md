# Step 8 - Final demonstration and handover

## Project and checked version
- Project: SC11 Water Quality Potability Example.
- Branch: step-8-final-demo, created from step-7-final-documentation.
- Tested published code/documentation commit: 1bd92a0.
- Date: 22 November 2026.
- Context: instructor technical rehearsal and handover preparation. No student assessment or faculty approval is claimed.

## Final checks
| Check | Evidence | Actual outcome |
| --- | --- | --- |
| Fresh published clone | Step 7 branch, commit 1bd92a0 | Cloned successfully; required model, metadata, report and slide files present |
| Validation | python -m unittest -v test_product_predict | Five tests passed in the cloned project |
| Saved CSV parity | python src/compare_step6_predictions.py | Nine inputs, class and label match on one saved sample |
| Document integrity | Compare SHA-256 of cloned files and local files | Report, PPTX and presentation PDF match exactly |
| Presentation | presentation/project_presentation.pptx | Eight slides; opened in PowerPoint; package/layout checks passed |
| Report | report/final_report.pdf | Four rendered pages visually checked |

Commands and outcomes: data/reports/step8_final_checks.txt. The tests used the separately installed Python 3.12.1 environment. This verifies the published files with that environment, not every operating system.

## Demonstration observations
These observations come from the technical browser rehearsal on a separate installed project copy. They are not a new formal audience demonstration.

| Case | What was shown | Observed result |
| --- | --- | --- |
| Normal | Existing validation sample | Class 1, readable label and educational notice |
| Upper pH boundary | Same input, pH changed to 14 | Accepted; class 0 |
| Invalid pH | Same input, pH changed to 15 | Range error; no prediction |
| New CSV download | Download button | Not verified: browser download stalled |
| Missing model | Historical Step 6 record | Not repeated in this rehearsal |

## Contributions and explanation
SC11 is an instructor teaching example by Bipul Kumar Shahi for the Soft Computing capstone workflow at Galgotias University. It has no allocated student team. The reference materials were prepared with AI assistance and checked against the saved project evidence.

Student teams should replace this statement with each real member's name, completed work, changed files, evidence and demonstration responsibility. Every member should explain the complete workflow, one design choice and one limitation.

## Remaining work and limits
- Repeat the new browser CSV download, save it to data/reports and compare against the same-input reference.
- Fix full-dataset imputation by splitting first, fitting preprocessing on training rows only, and retraining/reevaluating. Existing scores retain that limitation.
- Broaden app/reference checks beyond one saved CSV sample.
- A faculty demonstration, questions and approval must be recorded only after they actually happen.
- The prediction is educational and cannot certify drinking-water safety.

## Handover
- Code and UI: app.py and src/product_predict.py.
- Model and metadata: models/ann_water_potability.pkl and models/ann_model_metadata.json.
- Run instructions and direct versions: README.md and requirements-step7-runtime.txt.
- Report: report/final_report.md and report/final_report.pdf.
- Editable deck and reading copy: presentation/project_presentation.pptx and project_presentation.pdf.
- Final checks: data/reports/step8_final_checks.txt.
- Previous preparation and rehearsal: docs/STEP-7.md.
- Public showcase: not published; instructor chooses whether to publish. Students use their own project story and select the faculty/university mentions.
- Portal: no dummy student submission made for this unallocated instructor example.
