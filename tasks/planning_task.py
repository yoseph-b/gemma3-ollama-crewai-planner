from crewai import Task
from agents.planner_agent import planner
from utils.save_output import save_output

def save_planner_output(content):
    save_output("planner", content)

planning_task = Task(
    description="Analyze the user's prompt and break it into frontend, backend, database, and deployment tasks.",
    expected_output="A structured plan and architecture spec.",
    agent=planner,
    on_complete=save_planner_output
)
