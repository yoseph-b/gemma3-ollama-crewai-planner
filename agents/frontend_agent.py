import os
from crewai import Agent, LLM

llm = LLM(
    model="ollama/gemma3:270m",
    base_url="http://localhost:11434"
)

frontend = Agent(
    role='Frontend Engineer',
    goal='Generate a beautiful and functional user interface for the app idea using React and Tailwind CSS',
    backstory=(
        "You are a senior frontend engineer with a passion for clean, responsive, "
        "and accessible UIs. You are skilled in React, Tailwind CSS, and modern UI/UX principles. "
        "You turn specs into delightful frontend experiences."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)
