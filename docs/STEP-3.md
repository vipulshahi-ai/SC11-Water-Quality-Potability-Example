# SC11 Step 3 - ANN Model
## Goal
Train a feed-forward ANN using backpropagation to predict water potability.

## Inputs and output
- Inputs: pH, hardness, solids, chloramines, sulfate, conductivity,
organic carbon, trihalomethanes, and turbidity.
- Output: Potability (0 = not potable, 1 = potable).
- Architecture: 9 inputs -> 16 hidden neurons -> 8 hidden neurons -> 1 output.

## Data and evidence
Use the Step 2 train.csv, validation.csv, and test.csv files. Save metrics,
loss curve, confusion matrices, predictions, model, and metadata.

## Limitation
This educational model is not a replacement for laboratory analysis or official
water-safety certification.