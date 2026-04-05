from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

ACTIONS = ["work", "spam", "important", "personal"]

emails = [
    ("Team meeting at 10 AM", "work"),
    ("Win a free iPhone now!!!", "spam"),
    ("Project deadline tomorrow urgent", "work"),
    ("Dinner plans tonight?", "personal"),
    ("Your bank account needs verification", "spam")
]

last_email = None
last_label = None

class ActionInput(BaseModel):
    action: str

@app.post("/reset")
def reset():
    global last_email, last_label
    email, label = random.choice(emails)
    last_email = email
    last_label = label
    return {"observation": email, "valid_actions": ACTIONS}

@app.post("/step")
def step(input: ActionInput):
    global last_email, last_label
    action = input.action

    if action == last_label:
        reward = 1.0
    elif action in ["work", "important"] and last_label == "work":
        reward = 0.5
    else:
        reward = -1.0

    return {"reward": reward, "done": True}