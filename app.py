from fastapi import FastAPI
import random

app = FastAPI()

emails = [
    ("Team meeting at 10 AM", "work"),
    ("Win a free iPhone now!!!", "spam"),
    ("Project deadline tomorrow urgent", "work"),
    ("Dinner plans tonight?", "personal"),
    ("Your bank account needs verification", "spam")
]

@app.get("/")
def home():
    return {"message": "OpenEnv Email Triage Environment (Advanced)"}

@app.post("/reset")
def reset():
    email, label = random.choice(emails)
    return {
        "observation": email,
        "valid_actions": ["work", "spam", "important", "personal"],
        "correct": label
    }

@app.post("/step")
def step(data: dict):
    action = data.get("action")
    email = data.get("observation")

    correct_label = None
    for e, l in emails:
        if e == email:
            correct_label = l
            break

    if action == correct_label:
        reward = 1
        result = "correct"
    elif action in ["important", "work"] and correct_label == "work":
        reward = 0.5
        result = "partially correct"
    else:
        reward = -1
        result = "wrong"

    return {
        "email": email,
        "prediction": action,
        "correct": correct_label,
        "reward": reward,
        "result": result
    }