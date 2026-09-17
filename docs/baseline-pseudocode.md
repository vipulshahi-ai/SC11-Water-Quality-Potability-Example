READ one valid water sample row
IF the row is missing critical sensor data:
    SHOW a clear error (e.g., "Invalid Sensor Data")
ELSE:
    START risk_score at 0
    
    IF ph < 6.5 OR ph > 8.5: 
        ADD 1 to risk_score
    IF solids > 30000: 
        ADD 1 to risk_score
    IF turbidity > 5.0: 
        ADD 1 to risk_score
    
    IF risk_score == 0:
        PRINT "Baseline Output: Potable (Approve)"
    ELSE:
        PRINT "Baseline Output: Not Potable (Treat)"
        
SAVE the result for later comparison
