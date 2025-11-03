import pytest 
from tasks.task1.tools.data_pipeline import load_data, preprocess_data 
import numpy as np 

def test_no_leakage(): 
    X_train, X_test, y_train, y_test = load_data() 
    X_train_scaled, X_test_scaled = preprocess_data(X_train, X_test) 
    # Check if training data is properly standardized (mean~0, std~1)
    # If there's leakage, training data won't be perfectly standardized
    train_mean = np.mean(X_train_scaled) 
    train_std = np.std(X_train_scaled, ddof=1)
    assert abs(train_mean) < 0.1 and abs(train_std - 1.0) < 0.1, f"Training data not properly standardized: mean={train_mean:.3f}, std={train_std:.3f}" 

def test_shape_integrity(): 
    X_train, X_test, _, _ = load_data() 
    X_train_scaled, X_test_scaled = preprocess_data(X_train, X_test) 
    assert X_train_scaled.shape[1] == X_train.shape[1] 
    assert X_test_scaled.shape[1] == X_test.shape[1] 

def test_slow_edgecase(): 
    # Intentional fail: too strict condition 
    assert False, "Edgecase not implemented yet"