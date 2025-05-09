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
