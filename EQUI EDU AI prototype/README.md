EQUI EDU AI – Multi-Agent Learning Platform (Capstone \& Demo)

🚀 Project Overview

EQUI EDU AI is a beginner-friendly, modular multi-agent system designed to deliver personalized, accessible, and fair educational content for every learner.

Built with Python and Streamlit, it features agent orchestration, accessibility and equity simulation, input/output “memory”, and a user-friendly web UI.



✨ Features

Multi-Agent Orchestration: Each agent (content, assessment, accessibility, equity, motivation) specializes in one role and is coordinated by an orchestrator.



Agent Simulation \& Validation Loops: Simulates how real AI agents validate and regenerate their outputs.



Accessibility \& Fairness Checks: Supports simulated checks for dyslexia/audio needs and highlights content equity by user demographics.



User Interface: Clean, interactive web app powered by Streamlit.



Session “Memory”: Remembers recent learning sessions and displays input/output history.



Perfect for Demos \& YouTube: Designed for screen-sharing and explainer videos.



⚙️ How It Works

User enters learning topic, style, needs, and profile into a simple web form.



Orchestrator routes the request to one or more specialist agents.



Agents (Content, Assessment, Accessibility, Equity, Motivation) each generate output, run validations, and simulate adaptation for equity and accessibility.



Session Memory: All interactions are saved and displayed during the session.



🏁 Quick Start (Installation \& Usage)

bash

\# 1. Clone or download this repo.

git clone https://github.com/YOURUSERNAME/EQUI\_EDU\_AI.git

cd EQUI\_EDU\_AI



\# 2. Install Python dependencies

pip install streamlit pandas



\# 3. Start the web app!

streamlit run streamlit\_app.py

Open your browser to http://localhost:8501



📁 File Structure

text

EQUI\_EDU\_AI/

│

├── agents/

│   ├── content\_agent.py          # Handles explanations

│   ├── assessment\_agent.py       # Makes quizzes

│   ├── accessibility\_agent.py    # Makes everything accessible

│   ├── equity\_agent.py           # Fairness check

│   └── motivation\_agent.py       # Encouragement agent

│

├── orchestrator\_agent.py         # The “manager”

├── streamlit\_app.py              # The main UI app

├── README.md                     # This file!



💡 Example Usage Scenario

“I’m a student with dyslexia. I want to learn photosynthesis in a visual way and get a quiz. I also want it to be fair whatever my background.”



Enter this info in the Streamlit UI



Orchestrator runs content, accessibility, equity, assessment, and motivation agents



System response includes personalized explanation, fairness/accessibility notes, quiz, and a motivational message—all tracked in your session memory

