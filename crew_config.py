from dotenv import load_dotenv
load_dotenv()
from crewai import Crew
from agents.planner_agent import planner
from agents.frontend_agent import frontend
from agents.backend_agent import backend
from agents.db_agent import db
from agents.deploy_agent import deploy
from tasks.planning_task import planning_task
from tasks.frontend_task import frontend_task
from tasks.backend_task import backend_task
from tasks.db_task import db_task
from tasks.deploy_task import deploy_task

crew = Crew(
    agents=[planner, frontend, backend, db, deploy],
    tasks=[planning_task, frontend_task, backend_task, db_task, deploy_task],
    verbose=True
)
