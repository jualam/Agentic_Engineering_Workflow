# Agentic Engineering Workflow

Agentic Engineering Workflow is a CrewAI-based automation project that models a small software engineering team. It takes high-level product requirements and runs them through a sequential workflow that produces a backend module, a simple Gradio interface, and unit tests.

The project is designed as a practical example of agentic software development: each agent has a focused role, clear task ownership, and file-based outputs that can be reviewed, executed, and tested.

## Workflow

The crew runs four specialized agents in sequence:

- **Engineering Lead**: Creates a technical design from the provided requirements.
- **Backend Engineer**: Implements the backend Python module from the design.
- **Frontend Engineer**: Builds a lightweight Gradio demo for the generated backend.
- **Test Engineer**: Writes unit tests for the generated backend module.

Generated artifacts are written to the `output/` directory.

## Tech Stack

- Python 3.10+
- CrewAI
- Gradio
- Pytest
- Docker-backed safe code execution through CrewAI
- YAML-based agent and task configuration

## Getting Started

Clone the repository:

```bash
git clone https://github.com/jualam/Agentic_Engineering_Workflow.git
cd Agentic_Engineering_Workflow
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file in the project root and add your API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Usage

Run the CrewAI workflow:

```bash
uv run crewai run
```

You can also run the package entry point directly:

```bash
uv run agentic_engineering_workflow
```

After the workflow completes, review the generated files in `output/`.

## Project Structure

```text
.
+-- src/agentic_engineering_workflow/
|   +-- config/
|   |   +-- agents.yaml
|   |   +-- tasks.yaml
|   +-- crew.py
|   +-- main.py
+-- output/
+-- tests/
+-- pyproject.toml
+-- README.md
```

## Configuration

Agent roles, goals, and model settings are defined in `src/agentic_engineering_workflow/config/agents.yaml`.

Task descriptions, expected outputs, dependencies, and output file paths are defined in `src/agentic_engineering_workflow/config/tasks.yaml`.

## Output

For the default account-management example, the workflow generates:

- `output/accounts.py_design.md`
- `output/accounts.py`
- `output/app.py`
- `output/test_accounts.py`

These files represent the design document, backend implementation, demo UI, and unit tests created by the agent workflow.
