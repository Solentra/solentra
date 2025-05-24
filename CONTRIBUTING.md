# Contributing to Solentra

Thank you for your interest in contributing to Solentra! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Workflow](#contribution-workflow)
- [Code Style and Standards](#code-style-and-standards)
- [Documentation](#documentation)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Feature Requests and Bug Reports](#feature-requests-and-bug-reports)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/solentra.git
   cd solentra
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/solentra/solentra.git
   ```

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Contribution Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-fix-name
   ```

2. Make your changes following our [Code Style and Standards](#code-style-and-standards)

3. Write or update tests as needed

4. Update documentation if necessary

5. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request

## Code Style and Standards

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for all function parameters and return values
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names
- Include docstrings for all public functions and classes

Example:
```python
from typing import List, Dict, Optional

def analyze_data(
    data: List[float],
    confidence_level: float = 0.95
) -> Dict[str, float]:
    """
    Analyze numerical data and return statistical metrics.

    Args:
        data: List of numerical values to analyze
        confidence_level: Confidence level for statistical tests (default: 0.95)

    Returns:
        Dictionary containing statistical metrics
    """
    pass
```

### Documentation

- Use Markdown for all documentation files
- Follow the existing documentation structure in the `docs/` directory
- Include code examples where appropriate
- Keep documentation up to date with code changes

### Testing

- Write unit tests for all new features
- Maintain or improve test coverage
- Use pytest for testing
- Include both positive and negative test cases

Example test:
```python
def test_analyze_data():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = analyze_data(data)
    assert "mean" in result
    assert result["mean"] == 3.0
```
