import os
from crewai import Agent, LLM

llm = LLM(
    model="ollama/gemma3:270m",
    base_url="http://localhost:11434"
)

deploy = Agent(
    role='DevOps & Deployment Engineer',
    goal='Package and deploy the full-stack app using Docker and CI/CD',
    backstory=(
        "You are a DevOps and cloud deployment expert who sets up modern deployment pipelines. "
        "You can containerize applications using Docker, write docker-compose files, "
        "configure environment variables, and set up hosting instructions. "
        "You are also familiar with platforms like Railway, Vercel, and GitHub Actions."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)
