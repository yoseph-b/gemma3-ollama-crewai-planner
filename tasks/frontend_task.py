from crewai import Task
from agents.frontend_agent import frontend
from utils.save_output import save_output

def save_frontend_output(content):
    save_output("frontend", content)

frontend_task = Task(
    description=(
        "Take the user's prompt and the spec from the Planner. "
        "Design and write the full frontend application in React using Tailwind CSS. "
        "The UI should be fully functional, responsive, and include all necessary components "
        "(e.g., forms, buttons, pages, routing). Make sure code is modular and readable."
    ),
    expected_output=(
        "A complete React frontend app with component code, Tailwind styles, "
        "routing logic, and usage examples. Include a README for how to run it."
    ),
    agent=frontend,
    on_complete=save_frontend_output
)
