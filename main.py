from crew_config import crew

if __name__ == "__main__":
    prompt = input("What app do you want to build? ")
    crew.kickoff(inputs={"user_prompt": prompt})

