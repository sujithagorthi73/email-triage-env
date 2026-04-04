import random

class EmailEnv:
    def __init__(self):
        self.current = None
        self.level = "easy"

    def reset(self, level="easy"):
        self.level = level

        if level == "easy":
            self.emails = [
                {"text": "Team meeting at 10 AM", "label": "work"},
                {"text": "Movie tonight?", "label": "personal"},
            ]

        elif level == "medium":
            self.emails = [
                {"text": "Submit project report urgently", "label": "work"},
                {"text": "Your bank statement is ready", "label": "important"},
            ]

        else:
            self.emails = [
                {"text": "Win a free trip now!!!", "label": "spam"},
                {"text": "Urgent: verify your account now", "label": "spam"},
            ]

        self.current = random.choice(self.emails)
        return self.current["text"]

    def step(self, action):
        valid_actions = ["work", "spam", "important", "personal"]

        if action not in valid_actions:
            return {
                "error": "Invalid action",
                "valid_actions": valid_actions
            }, -1, True, {}

        correct = self.current["label"]

        if action == correct:
            reward = 1
            explanation = "Correct classification"
        elif action in ["work", "important"] and correct in ["work", "important"]:
            reward = 0.5
            explanation = "Close category"
        else:
            reward = -1
            explanation = "Wrong classification"

        if action == correct:
            confidence = 0.9
        elif action in ["work", "important"]:
            confidence = 0.6
        else:
            confidence = 0.3

        return {
            "email": self.current["text"],
            "prediction": action,
            "correct": correct,
            "reward": reward,
            "confidence": confidence,
            "priority": "high" if correct in ["work", "important"] else "low",
            "explanation": explanation,
            "valid_actions": valid_actions
        }, reward, True, {}

    def state(self):
        return self.current