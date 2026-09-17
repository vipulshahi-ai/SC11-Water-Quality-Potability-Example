import pandas as pd

FILE = 'data/sample_input.csv'
REQUIRED = ['sample_id', 'ph', 'hardness', 'solids', 'sulfate', 'turbidity', 'potability_target']
NUMERIC = ['ph', 'hardness', 'solids', 'sulfate', 'turbidity']

try:
    df = pd.read_csv(FILE)
    print('shape:', df.shape)
    print('columns:', list(df.columns))
    
    # Check for missing columns
    missing_columns = [c for c in REQUIRED if c not in df.columns]
    assert not missing_columns, f'Missing columns: {missing_columns}'
    
    # Check for missing values in required columns
    assert not df[REQUIRED].isna().any().any(), 'Missing value found! (Check WTR-005)'
    
    # Check numeric types
    for column in NUMERIC:
        assert pd.api.types.is_numeric_dtype(df[column]), f'{column} must be numeric'
        
    # Domain specific checks
    assert df['ph'].between(0, 14).all(), 'pH must be between 0 and 14'
    assert (df['solids'] >= 0).all(), 'Solids cannot be negative'
    
    print('STEP 1 DATA CHECK PASSED')

except AssertionError as e:
    print(f'VALIDATION FAILED: {e}')