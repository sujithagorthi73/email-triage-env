import requests

BASE_URL = "https://sujithagorthi-email-triage-env.hf.space"

print("START")

res = requests.post(BASE_URL + "/reset")
data = res.json()

obs = data["observation"]

print("STEP: 1")
print("Observation:", obs)

action = "work"

print("Action:", action)

res = requests.post(BASE_URL + "/step", json={"action": action})
print("Result:", res.json())

print("END")
