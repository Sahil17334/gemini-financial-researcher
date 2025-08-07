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
