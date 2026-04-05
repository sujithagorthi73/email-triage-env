import requests

BASE_URL = "https://sujithagorthi-email-triage-env.hf.space"

def main():
    print("START")

    res = requests.post(BASE_URL + "/reset")
    data = res.json()

    obs = data["observation"]

    print("STEP: 1")
    print("Observation:", obs)

    if "free" in obs.lower() or "win" in obs.lower():
        action = "spam"
    elif "meeting" in obs.lower() or "project" in obs.lower():
        action = "work"
    else:
        action = "personal"

    print("Action:", action)

    res = requests.post(BASE_URL + "/step", json={"action": action})
    result = res.json()

    print("Result:", result)

    print("END")

if __name__ == "__main__":
    main()