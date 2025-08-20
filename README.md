# CrewAI Planning Engineer (Ollama Gemma3)

A lightweight CrewAI agent that breaks down app requests into detailed specifications and subtasks, powered by a local Ollama LLM (Gemma3:270m).

## Features
- Decomposes app prompts into architecture and implementation subtasks
- Runs locally via Ollama (no external API keys)
- Simple, extensible Python setup

## Project Structure

Key file: `agents/planner_agent.py` defines the Planning Engineer agent and local LLM config.

## Prerequisites
- Python 3.10+ (Windows)
- [Ollama](https://ollama.com/) installed and running
- Gemma3 model available locally (`gemma3:270m`)

## Setup

1) Install and start Ollama (Windows):
- Install via installer from the Ollama website, then start Ollama.
- Pull the model (first run will pull automatically):
```powershell
ollama pull gemma3:270m
```

2) Create and activate a virtual environment:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Install dependencies:
```powershell
pip install crewai
```
If you later add a `requirements.txt`, use:
```powershell
pip install -r requirements.txt
```

## Configuration
Model and endpoint are configured in `agents/planner_agent.py`. Default:
```python
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
```

- Change `model` if you use a different local model (e.g., `ollama/gemma2:2b`).
- Ensure `base_url` matches your Ollama server URL.

## Usage

Example with CrewAI `Task` and `Crew`:
```python
from crewai import Task, Crew
from agents.planner_agent import planner

task = Task(
    description="Break down a 'Todo app with auth and offline sync' into full specs and subtasks",
    agent=planner
)

crew = Crew(agents=[planner], tasks=[task])
result = crew.kickoff()
print(result)
```

Or import the `planner` directly and integrate into your own pipeline.

## Troubleshooting
- Ollama not reachable: ensure the Ollama service is running and `base_url` is `http://localhost:11434`.
- Model not found: run `ollama pull gemma3:270m` or switch to an installed model.
- Permission issues on Windows PowerShell: you may need `Set-ExecutionPolicy -Scope Process RemoteSigned` before activating the venv.

## Roadmap
- Add CLI for prompt input and JSON spec output
- Persist plans to files
- Add more specialized agents (e.g., Reviewer, Architect)

