# gemini-financial-researcher
A multi agent financial research assistant that uses Gemini API and crewAI to generate comprehensive financial reports. This project uses agentic workflows, RAG with real time data, and integration with external APIs. It is designed to be a modular and scalable solution for automated financial analysis.

AI Financial Research Crew
An advanced financial analysis tool powered by a crew of autonomous AI agents. This project leverages Google's Gemini Pro and the crewAI framework to automate the process of researching and analyzing financial data for any given company, delivering comprehensive and insightful reports.

Overview
This project demonstrates a sophisticated multi-agent system designed for financial intelligence. It operationalizes an agentic workflow where a Researcher Agent first gathers real-time data and news, which a Financial Analyst Agent then synthesizes into a detailed report. This showcases a practical application of Large Language Models for complex, real-world tasks.

Key Features
Multi-Agent System: Utilizes a crew of specialized AI agents (Researcher & Analyst) that collaborate to achieve a common goal.

Powered by Google Gemini: Leverages the advanced reasoning and text generation capabilities of the Gemini family of models.

Real-time Data Integration: Integrates with SerperDevTool for up-to-the-minute search results, ensuring the analysis is based on current information.

Modular & Configurable: Agents and tasks are defined in simple YAML files (agents.yaml, tasks.yaml), making the crew's behavior easy to modify and extend.

Secure API Key Management: Ensures your secret API keys are kept safe using a .env file, which is ignored by Git.

Project Architecture
The workflow is executed sequentially:

Input: The user provides a company name.

Research Task: The Researcher Agent is activated. It uses its search tool to gather financial data, news, and market trends related to the company.

Analysis Task: The output from the Researcher is passed to the Financial Analyst Agent. This agent analyzes the gathered information, structures it, and drafts the final comprehensive report.

Output: The final report is printed to the console.

Technology Stack
Backend: Python

AI Framework: crewAI

LLM: Google Gemini

Search Tool: Serper

Dependency Management: Poetry / pip

Cloning and Running Instructions
Follow these steps to get the project set up and running on your local machine.

1. Prerequisites
Python 3.10 or higher

git installed on your system

API Keys for:

Google AI (Gemini)

Serper.dev (for the search tool)

2. Clone the Repository
Open your terminal and run the following command to clone the project:

Bash

git clone https://github.com/YOUR_USERNAME/financial-researcher.git
cd financial-researcher
(Replace YOUR_USERNAME with your actual GitHub username.)

3. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
4. Install Dependencies
Install all the required Python packages using the pyproject.toml file.

Bash

pip install .
5. Configure Environment Variables
Your secret API keys are managed through an environment file.

Create a new file named .env in the root directory of the project. You can do this by copying the example file:

Bash

cp .env.example .env
Open the newly created .env file with a text editor.

Paste your API keys into the file as shown below:

Code snippet

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
SERPER_API_KEY="YOUR_SERPER_API_KEY_HERE"
6. Run the Application
You are now ready to run the financial research crew! Execute the main script from your terminal:

Bash

python src/financial_researcher/main.py
The application will then prompt you to enter the name of the company you wish to analyze. Sit back and watch the AI crew work!
