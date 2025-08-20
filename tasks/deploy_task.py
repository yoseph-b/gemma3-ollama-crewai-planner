from crewai import Task
from agents.deploy_agent import deploy
from utils.save_output import save_output

def save_deploy_output(content):
    save_output("deploy", content)

deploy_task = Task(
    description=(
        "Based on the frontend, backend, and database setup, write Dockerfiles for both frontend and backend. "
        "If needed, generate a docker-compose.yml to orchestrate services. "
        "Include a README with instructions to build, run, and deploy the app. "
        "Also suggest deployment platforms (like Railway, Vercel, or Fly.io) and optionally include CI/CD configs."
    ),
    expected_output=(
        "- `Dockerfile` for backend (FastAPI) and frontend (React)\n"
        "- `docker-compose.yml` for local orchestration\n"
        "- `.env.example` for environment variables\n"
        "- `README.md` with full deployment instructions\n"
        "- Optional: GitHub Actions config for CI/CD"
    ),
    agent=deploy,
    on_complete=save_deploy_output
)
