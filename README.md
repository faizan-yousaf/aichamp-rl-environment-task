# AIChamp RL Task – Data Leakage Fix Challenge 

**Objective**
Design an RL environment that challenges the model to identify and fix a data preprocessing bug that causes data leakage.

**Project Layout**
```
hello-py/
├── tasks/
│   └── task1/
│       ├── prompt.md
│       ├── grader.py
│       ├── tools/
│       │   └── data_pipeline.py
│       └── tests/
│           └── test_preprocessing.py
├── evaluate.py
├── README.md
├── time_log.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

**Run Locally**
- Install deps: `pip install -r requirements.txt`
- Run tests: `python -m pytest tasks/task1/tests/test_preprocessing.py -v`
- Run grader: `python tasks/task1/grader.py` (expects PASS: no_leakage passed; slow_edgecase failed)
- Run evaluation: `python evaluate.py` (creates `results.csv` and `submission/` outputs)

**Environment Variables**
- Create `.env` with: `ANTHROPIC_API_KEY=your_api_key_here`
- A sample `.env.example` is provided; `.env` is gitignored.

**Success Criteria**
A successful model run should fix the bug so:
- `test_no_leakage` → PASSES
- `test_slow_edgecase` → FAILS (intentionally)
- Overall pass rate after 20 runs should be between 10–40%

**Submission Instructions**
1. Ensure grader PASS locally: `python tasks/task1/grader.py`
2. Run evaluation to generate `results.csv`: `python evaluate.py`
3. Include these in your submission:
   - Task folder `tasks/task1/`
   - `grader.py`, `prompt.md`, `tools/data_pipeline.py`, `tests/test_preprocessing.py`
   - Root `evaluate.py`, `README.md`, `time_log.md`, `requirements.txt`
   - `results.csv` from evaluation
4. Share via GitHub or Google Drive link.
5. Fill out the short contractor form with your link.

**Notes**
- `submission/` and `*.csv` are ignored by git but included in your submission archive.
- Use Python `sys.executable` and `-m pytest` in CI for reliable runs on Windows.
