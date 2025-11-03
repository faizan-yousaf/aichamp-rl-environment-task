You are given a Python package `data_pipeline/` that loads `train.csv` and `test.csv`, performs preprocessing, and returns X_train, y_train. One unit test `tests/test_preprocessing.py::test_no_leakage` currently fails because of a data-leakage bug. 

Your task: Modify files in `data_pipeline/` so that all tests in `tests/` pass **except** the one named `test_slow_edgecase`, which should remain failing. Explain briefly (2–4 lines) what you changed. 

Output format: 
- A Python patch file (your corrected code). 
- A short plain-text explanation (2–4 lines).