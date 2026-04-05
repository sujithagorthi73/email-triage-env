import requests

BASE_URL = "https://sujithagorthi-email-triage-env.hf.space"

def main():
    print("START")

    # RESET
    res = requests.post(f"{BASE_URL}/reset")
    data = res.json()

    observation = data["observation"]
    print(f"STEP: 1")
    print(f"Observation: {observation}")

    # Rule-based action
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

    print(f"Result: {result}")

    print("END")

if __name__ == "__main__":
    main()