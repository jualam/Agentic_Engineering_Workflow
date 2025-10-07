# Agentic Engineering Workflow (AEW)

Agentic Engineering Workflow (AEW) is an autonomous multi-agent engineering pipeline that automates the full software development process from design to deployment using the CrewAI agentic framework.

AEW simulates a collaborative engineering team composed of specialized AI agents, each with a defined role and goal. Working sequentially, these agents transform high-level requirements into a complete, working software system.

## System Overview

- **Engineering Lead**: Converts high-level requirements into a detailed technical design and module specification.  
- **Backend Engineer**: Implements a fully self-contained Python module following the design, safely executed inside Docker-isolated environments.  
- **Frontend Engineer**: Builds a lightweight Gradio UI to demonstrate the backend logic and user interaction.  
- **Test Engineer**: Writes and runs unit tests to validate correctness, functionality, and reliability.

All agents operate under a CrewAI sequential workflow, enabling fully automated code generation, integration, and testing, producing ready-to-run software artifacts and UI demos.

## Tech Stack

**Languages and Frameworks**
- Python  
- CrewAI (multi-agent framework)  
- Gradio (frontend demo UI)  

**Tools and Environments**
- Docker (safe code execution sandbox)  
- YAML (agent and task configuration)  
- Pytest (unit testing)  
- OOP (modular architecture)

## Features

- Fully autonomous multi-agent collaboration workflow  
- Design to Implementation to Frontend to Testing all in one run  
- Sandbox code execution using Docker for safety  
- Automatically generated Gradio UI for demonstration  
- Configurable agents and tasks via YAML  
- Modular, self-contained Python modules for easy testing and extension

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/jualam/Agentic_Engineering_Workflow.git
   cd Agentic_Engineering_Workflow
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt or uv sync
   
3. Add your API keys in a .env file:
OPENAI_API_KEY=your_openai_key


5. Start the application: crewai run
