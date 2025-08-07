import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import yaml

# Load environment variables from .env file
load_dotenv()

# Ensure the GEMINI_API_KEY is set
if "GEMINI_API_KEY" not in os.environ:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it.")

# Initialize the search tool
search_tool = SerperDevTool()

# Load agent and task configurations from YAML files
with open('config/agents.yaml', 'r') as file:
    agents_config = yaml.safe_load(file)

with open('config/tasks.yaml', 'r') as file:
    tasks_config = yaml.safe_load(file)

# Create the researcher agent
researcher_config = agents_config['researcher']
researcher = Agent(
    role=researcher_config['role'],
    goal=researcher_config['goal'],
    backstory=researcher_config['backstory'],
    llm_config={"model": researcher_config['llm']['model']},
    tools=[search_tool],
    allow_delegation=researcher_config['allow_delegation'],
    verbose=researcher_config.get('verbose', True)
)

# Create the analyst agent
analyst_config = agents_config['analyst']
analyst = Agent(
    role=analyst_config['role'],
    goal=analyst_config['goal'],
    backstory=analyst_config['backstory'],
    llm_config={"model": analyst_config['llm']['model']},
    allow_delegation=analyst_config['allow_delegation'],
    verbose=analyst_config.get('verbose', True)
)

# Create tasks for the agents
research_task_config = tasks_config['research_company_task']
research_task = Task(
    description=research_task_config['description'],
    expected_output=research_task_config['expected_output'],
    agent=researcher
)

analysis_task_config = tasks_config['analyze_company_task']
analysis_task = Task(
    description=analysis_task_config['description'],
    expected_output=analysis_task_config['expected_output'],
    agent=analyst
)

# Instantiate your crew with a sequential process
financial_crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential,
    verbose=2
)

def run():
    """
    Asks the user for a company name and runs the financial crew.
    """
    company = input("What company would you like to research? ")
    result = financial_crew.kickoff(inputs={'company': company})
    print("\n\n########################")
    print("## Here is the Final Report:")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run()
