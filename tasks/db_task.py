from crewai import Task
from agents.db_agent import db
from utils.save_output import save_output

def save_db_output(content):
    save_output("database", content)

db_task = Task(
    description=(
        "Based on the project spec, design a relational database schema using PostgreSQL or SQLite. "
        "Define all tables, fields, primary keys, foreign keys, and relationships. "
        "Generate the schema in SQL or SQLAlchemy format. "
        "Include a `schema.sql` or `models.py` file and a brief explanation of the schema design. "
        "Optionally include seed data if applicable."
    ),
    expected_output=(
        "- Complete database schema in SQL or SQLAlchemy\n"
        "- Clear relationships between tables (e.g., OneToMany, ManyToMany)\n"
        "- Sample insert statements (optional)\n"
        "- Database connection code or `.env` file example\n"
        "- README instructions for setting up the DB"
    ),
    agent=db,
    on_complete=save_db_output
)
