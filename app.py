from fastapi import FastAPI
from pydantic import BaseModel
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

# Store state
last_email = None
last_label = None

class ActionInput(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "OpenEnv Email Triage Environment (Advanced)"}

# RESET endpoint
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

# STEP endpoint (FIXED)
@app.post("/step")
def step(input: ActionInput):
    global last_email, last_label

    action = input.action

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
