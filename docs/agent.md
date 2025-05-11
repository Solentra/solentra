# SolentraAgent Documentation

## Overview

The `SolentraAgent` class is the core component of the Solentra package, providing a powerful interface for creating and managing AI agents specialized in scientific research and experimentation.

## Installation

```bash
pip install solentra
```

## Basic Usage

```python
from solentra import SolentraAgent

# Initialize with default settings
agent = SolentraAgent(
    agent_name="Research Scientist",
    model_name="solentra-70b",
    tools_enabled=True
)

# Generate a response
response = agent.generate_response(
    "Explain quantum tunneling in enzyme catalysis"
)
```

## Core Features

### Agent Initialization

```python
agent = SolentraAgent(
    agent_name="Default Scientist",  # Name of the agent
    model_name="solentra-70b",      # Model to use
    tools_enabled=True,             # Enable scientific tools
    interactive=True,               # Enable interactive mode
    streaming_on=True,              # Enable response streaming
    temperature=0.7,                # Response randomness (0-1)
    max_tokens=150,                 # Maximum response length
    use_context=True,               # Enable conversation memory
    persona=None,                   # Predefined persona
    logging_enabled=False           # Enable logging
)
```

### Response Generation

```python
# Basic response
response = agent.generate_response("Explain protein folding")

# With context
agent.learn("topic", "details")
response = agent.generate_response("What do you know about the topic?")
```

### Experiment Management

```python
# Create experiment protocol
protocol = agent.create_experiment(
    steps=["Setup", "Measure", "Analyze"],
    materials=["Sample A", "Detector"],
    duration="1 hour",
    conditions={"temperature": 25}
)

# Run experiment
results = agent.run_experiment(
    protocol=protocol,
    variables={"concentration": 0.5},
    iterations=3
)
```

### Data Analysis

```python
# Analyze experimental data
data = [1.2, 1.3, 1.1, 1.4, 1.2]
analysis = agent.analyze_data(data, confidence_level=0.95)
```

### Research Task Planning

```python
# Create research plan
plan = agent.plan_research_task(
    objective="Study enzyme kinetics",
    subtasks=["Literature review", "Data collection"],
    dependencies={"Data collection": ["Literature review"]}
)

# Update progress
agent.update_task_progress(["task-1"])
```

### Paper Analysis

```python
# Analyze research paper
paper_text = """
Title: Quantum Effects in Biology
Abstract: This study investigates quantum phenomena in biological processes.
Keywords: quantum biology, coherence
"""
metadata = agent.analyze_paper(paper_text)
```

### Citation Management

```python
# Format citation
citation = agent.format_citation(
    authors=["Smith, J"],
    title="Study Title",
    journal="Journal Name",
    year=2023,
    doi="10.1234/paper"
)
```

### Multi-Agent Collaboration

```python
# Create specialized agents
physicist = SolentraAgent(persona="physicist")
biologist = SolentraAgent(persona="biologist")

# Collaborate
discussion = agent.collaborate(
    other_agent=physicist,
    prompt="Discuss quantum effects in biology",
    turns=3
)
```
