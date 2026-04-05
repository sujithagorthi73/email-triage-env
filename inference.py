import requests

BASE_URL = "https://sujithagorthi-email-triage-env.hf.space"

def run_episode():
    print("START")

    # RESET
    res = requests.post(f"{BASE_URL}/reset")
    data = res.json()

    observation = data["observation"]
    valid_actions = data["valid_actions"]

    print(f"Observation: {observation}")

    # Simple rule-based agent
    if "free" in observation.lower() or "win" in observation.lower():
        action = "spam"
    elif "meeting" in observation.lower() or "project" in observation.lower():
        action = "work"
    else:
        action = "personal"

    print(f"Action: {action}")

    # STEP
    res = requests.post(f"{BASE_URL}/step", json={"action": action})
    result = res.json()

    print("Result:", result)
    print("END")

if __name__ == "__main__":
    run_episode()