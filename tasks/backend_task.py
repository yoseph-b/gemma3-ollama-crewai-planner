from crewai import Task
from agents.backend_agent import backend
from utils.save_output import save_output

def save_backend_output(content):
    save_output("backend", content)

backend_task = Task(
    description=(
        "Using the app specification and user prompt, design a backend using FastAPI. "
        "The backend should include API routes, user authentication if needed, error handling, "
        "and integration with a database (PostgreSQL or SQLite). "
        "Structure the code with routers, models, and services folders. "
        "Include a Dockerfile and README explaining how to run the backend locally."
    ),
    expected_output=(
        "A complete FastAPI backend application with the following:\n"
        "- Main app entrypoint (main.py)\n"
        "- `routers/` folder with route files\n"
        "- `models/` folder with Pydantic models\n"
        "- `services/` for business logic\n"
        "- Config for database connection\n"
        "- Dockerfile\n"
        "- README with setup instructions"
    ),
    agent=backend,
    on_complete=save_backend_output
)
