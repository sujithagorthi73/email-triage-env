import requests

BASE_URL = "https://sujithagorthi-email-triage-env.hf.space"

def main():
    print("START")

    try:
        # RESET
        res = requests.post(f"{BASE_URL}/reset")
        data = res.json()

        observation = data.get("observation")
        print("STEP: 1")
        print(f"Observation: {observation}")

        # simple agent
        if observation and ("free" in observation.lower() or "win" in observation.lower()):
            action = "spam"
        elif observation and ("meeting" in observation.lower() or "project" in observation.lower()):
            action = "work"
        else:
            action = "personal"

        print(f"Action: {action}")

        # STEP
        res = requests.post(f"{BASE_URL}/step", json={"action": action})
        result = res.json()

        print(f"Result: {result}")

    except Exception as e:
        print("ERROR:", str(e))

    print("END")


if __name__ == "__main__":
    main()