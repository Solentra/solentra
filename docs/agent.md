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
