import pandas as pd 
from sklearn.preprocessing import StandardScaler 

def load_data(): 
    train = pd.read_csv("tasks/task1/data/train.csv") 
    test = pd.read_csv("tasks/task1/data/test.csv") 
    X_train = train.drop("target", axis=1) 
    y_train = train["target"] 
    X_test = test.drop("target", axis=1) 
    y_test = test["target"] 
    return X_train, X_test, y_train, y_test 

def preprocess_data(X_train, X_test): 
    # Fix: Fit scaler only on training data, then transform both sets
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled