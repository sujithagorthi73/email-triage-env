from env.email_env import EmailEnv

env = EmailEnv()

for level in ["easy", "medium", "hard"]:
    print(f"\n--- {level.upper()} LEVEL ---")

    obs = env.reset(level)
    print("Email:", obs)

    for action in ["work", "spam", "important", "personal"]:
        print(f"\nTrying action: {action}")
        result = env.step(action)
        print(result[0])