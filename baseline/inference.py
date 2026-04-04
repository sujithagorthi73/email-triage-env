import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from env.email_env import EmailEnv

# REQUIRED VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")  # no default

# OPTIONAL
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

def run():
    print("START")

    env = EmailEnv()
    total_reward = 0

    for level in ["easy", "medium", "hard"]:
        print(f"\nSTEP: {level}")

        obs = env.reset(level)
        print("Observation:", obs)

        # simple rule-based baseline
        if "meeting" in obs.lower():
            action = "work"
        elif "free" in obs.lower() or "offer" in obs.lower():
            action = "spam"
        elif "bank" in obs.lower() or "account" in obs.lower():
            action = "important"
        else:
            action = "personal"

        result, reward, done, _ = env.step(action)

        print("Action:", action)
        print("Result:", result)

        total_reward += reward

    print("\nEND")
    print("Total Reward:", total_reward)


if __name__ == "__main__":
    run()