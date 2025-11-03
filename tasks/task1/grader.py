import subprocess 
import sys 

def run_tests(): 
    # Use verbose mode so test names and statuses appear explicitly
    result = subprocess.run([sys.executable, "-m", "pytest", "-v", "tasks/task1/tests/test_preprocessing.py"], capture_output=True, text=True)
    output = result.stdout + result.stderr

    passed_no_leakage = "test_no_leakage PASSED" in output
    failed_edgecase = "test_slow_edgecase FAILED" in output

    if passed_no_leakage and failed_edgecase:
        print("PASS")
        sys.exit(0)
    else:
        print("FAIL")
        print(output)
        sys.exit(1) 

if __name__ == "__main__": 
    run_tests()