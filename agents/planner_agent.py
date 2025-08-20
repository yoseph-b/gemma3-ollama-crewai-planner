import os
from crewai import Agent, LLM

llm = LLM(
    model="ollama/gemma3:270m",
    base_url="http://localhost:11434"
)

planner = Agent(
    role='Planning Engineer',
    goal='Break down the app request into full specs and assign subtasks',
    backstory="Expert at analyzing prompts and planning full app architecture",
    verbose=True,
    allow_delegation=True,
    llm=llm
)
