import os
from crewai import Agent, LLM

llm = LLM(
    model="ollama/gemma3:270m",
    base_url="http://localhost:11434"
)

db = Agent(
    role='Database Designer',
    goal='Design the complete database schema with relationships and connection config',
    backstory=(
        "You are a database expert specializing in PostgreSQL and SQLite. "
        "You know how to convert business requirements into normalized, scalable database schemas. "
        "You write clean schema definitions and can generate SQLAlchemy or raw SQL as needed. "
        "You're also familiar with database connection setup and migrations."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)
