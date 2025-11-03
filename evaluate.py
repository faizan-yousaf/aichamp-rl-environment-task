import os, subprocess, csv, time, sys
from anthropic import Anthropic 
from dotenv import load_dotenv 

load_dotenv() 
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 

PROMPT_PATH = "tasks/task1/prompt.md" 

MODEL_NAME = os.getenv("MODEL_NAME", "claude-3-5-sonnet-20241022")

def call_model(prompt): 
    try:
        message = client.messages.create(
            model=MODEL_NAME,
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        # Graceful offline fallback: return an error marker string
        return f"API_ERROR: {e}" 

def run_once(i): 
    prompt = open(PROMPT_PATH).read() 
    t0 = time.time() 
    output = call_model(prompt) 
    os.makedirs("submission", exist_ok=True)
    with open(f"submission/output_{i}.txt", "w") as f: 
        f.write(output) 
    rc = subprocess.run([sys.executable, "tasks/task1/grader.py"]) 
    passed = (rc.returncode == 0) 
    return time.time() - t0, passed 

def main(): 
    results = [] 
    runs = int(os.getenv("EVAL_RUNS", "20"))
    for i in range(runs): 
        t, ok = run_once(i) 
        results.append([i, t, ok]) 
    with open("results.csv", "w", newline="") as f: 
        writer = csv.writer(f) 
        writer.writerow(["run", "time", "pass"]) 
        writer.writerows(results) 
 
if __name__ == "__main__": 
    main()