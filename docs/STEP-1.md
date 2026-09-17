# Step 1 Project Contract

## Team and responsibilities
- Student 1 - Repository setup and GitHub management
- Student 2 - Data Dictionary and Sample Fixtures
- Student 3 - Baseline Rules and Validation Testing
- Student 4 - UI Wireframe and Documentation

## One-sentence problem
Given water chemistry metrics, predict if the water sample is potable and safe for human consumption.

## User of the product
A water plant operator deciding whether to flag a water source for purification.

## Inputs and units
- ph: number (0-14)
- hardness: mg/L
- solids: ppm
- sulfate: mg/L
- turbidity: NTU

## Outputs and units
potability_class (Potable / Not Potable), confidence_score (0-100%), required_action (Approve / Treat)

## Baseline method
A fixed-threshold rule system based on standard safety limits for pH and dissolved solids.

## Soft Computing method for M1
An ANN classifier or Fuzzy Logic inference system compared against the fixed-threshold baseline.

## Advanced method for M2
Use a Genetic Algorithm (GA) to optimize the classification weights, test against missing sensor data, and deploy the app.
