from fastapi import FastAPI
import random

app = FastAPI()

# Possible actions
ACTIONS = ["work", "spam", "important", "personal"]

# Email dataset
emails = [
    ("Team meeting at 10 AM", "work"),
    ("Win a free iPhone now!!!", "spam"),
    ("Project deadline tomorrow urgent", "work"),
    ("Dinner plans tonight?", "personal"),
    ("Your bank account needs verification", "spam")
]

# Store last state
last_email = None
last_label = None

@app.get("/")
def home():
    return {"message": "OpenEnv Email Triage Environment (Advanced)"}

# RESET (OpenEnv calls this first)
@app.post("/reset")
def reset():
    global last_email, last_label

    email, label = random.choice(emails)
    last_email = email
    last_label = label

    return {
        "observation": email,
        "valid_actions": ACTIONS
    }

# STEP (OpenEnv sends only action)
@app.post("/step")
def step(data: dict):
    global last_email, last_label

    action = data.get("action")

    # Reward logic
    if action == last_label:
        reward = 1.0
        result = "correct"
    elif action in ["work", "important"] and last_label == "work":
        reward = 0.5
        result = "partially correct"
    else:
        reward = -1.0
        result = "wrong"

    return {
        "email": last_email,
        "prediction": action,
        "correct": last_label,
        "reward": reward,
        "result": result,
        "done": True
    }

# OPTIONAL: simple evaluation endpoint (extra strength)
@app.get("/evaluate")
def evaluate():
    total = 0
    trials = 5

    for _ in range(trials):
        email, label = random.choice(emails)

        if "free" in email.lower():
            pred = "spam"
        elif "meeting" in email.lower() or "project" in email.lower():
            pred = "work"
        else:
            pred = "personal"

        if pred == label:
            total += 1
        elif pred in ["work", "important"] and label == "work":
            total += 0.5

    return {
        "trials": trials,
        "score": total,
        "average": round(total / trials, 2)
    }