import os
from crewai import Agent, LLM

llm = LLM(
    model="ollama/gemma3:270m",
    base_url="http://localhost:11434"
)

backend = Agent(
    role='Backend Engineer',
    goal='Design and implement a secure, scalable RESTful backend using FastAPI',
    backstory=(
        "You are a seasoned backend engineer who excels at building clean and scalable RESTful APIs. "
        "You are highly experienced in Python, FastAPI, authentication, validation, error handling, and REST standards. "
        "You know how to structure projects and connect with PostgreSQL or SQLite databases."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)
