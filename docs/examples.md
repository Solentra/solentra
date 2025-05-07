# Examples

This document provides examples of using the Solentra package for various scientific research and experimentation tasks.

## Table of Contents
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Scientific Usage](#scientific-usage)
- [Best Practices](#best-practices)
- [Notes](#notes)

## Basic Usage

### Agent Initialization

```python
from solentra import SolentraAgent

# Basic initialization
agent = SolentraAgent(
    agent_name="Research Scientist",
    model_name="solentra-70b",
    tools_enabled=True
)

# With persona
physicist = SolentraAgent(
    persona="physicist",
    temperature=0.7,
    max_tokens=200
)
```

### Response Generation

```python
# Basic response
response = agent.generate_response("Explain quantum tunneling")

# With context
agent.learn("quantum_tunneling", "A quantum mechanical phenomenon")
response = agent.generate_response("What is quantum tunneling?")
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

## Advanced Usage


### Multi-Agent Collaboration

```python
# Create specialized agents
physicist = SolentraAgent(persona="physicist")
biologist = SolentraAgent(persona="biologist")
chemist = SolentraAgent(persona="chemist")

# Sequential collaboration
physics_view = physicist.generate_response(
    "Explain quantum tunneling in enzymes"
)

biology_view = biologist.generate_response(
    f"Based on physics: {physics_view}\n"
    "How might this affect enzyme function?"
)

chemistry_view = chemist.generate_response(
    f"Given these insights:\n"
    f"Physics: {physics_view}\n"
    f"Biology: {biology_view}\n"
    "What detection methods could we use?"
)
```

### Complex Experiment Workflow

```python
# Create detailed protocol
protocol = agent.create_experiment(
    steps=[
        "Prepare protein samples",
        "Calibrate equipment",
        "Measure baseline",
        "Record measurements"
    ],
    materials=[
        "Purified enzyme (1mg/mL)",
        "Buffer solution (pH 7.4)",
        "UV-Vis spectrophotometer"
    ],
    conditions={
        "temperature": 37,
        "pH": 7.4
    }
)

# Run multiple iterations
results = agent.run_experiment(
    protocol=protocol,
    variables={
        "concentration": [0.1, 0.5, 1.0],
        "time": [0, 5, 10, 15]
    },
    iterations=3
)
```

### Research Paper Analysis

```python
# Sample paper text
paper_text = """
Title: Quantum Effects in Enzyme Catalysis

Abstract: This study investigates quantum mechanical phenomena in enzyme
catalysis, focusing on proton tunneling effects. Our findings suggest that
quantum tunneling plays a significant role in reaction rates, particularly
at low temperatures.

Keywords: quantum biology, enzyme catalysis, proton tunneling
"""

# Analyze paper
metadata = agent.analyze_paper(paper_text)

# Extract key points
key_points = agent.extract_key_points(paper_text)

# Suggest related topics
topics = agent.suggest_related_topics("quantum enzyme catalysis")
```

### Social Media Integration

```python
# Initialize agent with Twitter config
twitter_config = {
    'api_key': 'your_api_key',
    'api_secret': 'your_api_secret',
    'access_token': 'your_access_token',
    'access_token_secret': 'your_access_token_secret'
}

agent = SolentraAgent(twitter_config=twitter_config)

# Post research update
tweet = agent.post_tweet(
    "Exciting new results from our quantum biology experiments! 🧬✨",
    media_paths=["results_graph.png"]
)

# Schedule future update
from datetime import datetime, timedelta
future = datetime.now() + timedelta(days=1)
scheduled = agent.schedule_tweet(
    "Join us tomorrow for our quantum biology seminar! 🎓",
    scheduled_time=future
)

# Analyze engagement
metrics = agent.analyze_tweet_engagement(tweet['id'])
```

## Scientific Usage

### Quantum Biology Experiment

```python
# Create experiment protocol
protocol = agent.create_experiment(
    steps=[
        "Prepare enzyme samples at 5°C",
        "Set up quantum detection apparatus",
        "Measure tunneling rates",
        "Record quantum coherence times"
    ],
    materials=[
        "Purified enzyme (1mg/mL)",
        "Quantum detection system",
        "Temperature control unit"
    ],
    conditions={
        "temperature": 5,
        "pH": 7.4
    }
)

# Run experiment
results = agent.run_experiment(
    protocol=protocol,
    variables={
        "tunneling_rate": [0.1, 0.2, 0.3],
        "coherence_time": [100, 150, 200]
    },
    iterations=3
)
```

### Protein Folding Analysis

```python
# Sample protein data
protein_data = {
    "sequence": "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN",
    "structure": "Alpha-helix dominant with beta-sheets",
    "properties": {
        "molecular_weight": 5807.7,
        "isoelectric_point": 5.5,
        "stability": 0.8
    }
}

# Analyze protein
analysis = agent.analyze_data(
    [protein_data["properties"]["stability"]],
    confidence_level=0.95
)

# Generate insights
insights = agent.generate_response(
    f"Based on the protein sequence and structure:\n"
    f"Sequence: {protein_data['sequence']}\n"
    f"Structure: {protein_data['structure']}\n"
    "What are the key structural features and potential functional implications?"
)
```

### Research Literature Review

```python
# Sample paper collection
papers = [
    {
        "title": "Quantum Effects in Enzyme Catalysis",
        "abstract": "This study investigates quantum mechanical phenomena in enzyme catalysis, focusing on proton tunneling effects.",
        "keywords": ["quantum biology", "enzyme catalysis", "proton tunneling"]
    },
    {
        "title": "Protein Folding Mechanisms",
        "abstract": "Analysis of protein folding pathways and energy landscapes using molecular dynamics simulations.",
        "keywords": ["protein folding", "molecular dynamics", "energy landscape"]
    }
]

# Analyze papers
for paper in papers:
    metadata = agent.analyze_paper(
        f"Title: {paper['title']}\n"
        f"Abstract: {paper['abstract']}\n"
        f"Keywords: {', '.join(paper['keywords'])}"
    )
    
    # Extract key points
    key_points = agent.extract_key_points(paper['abstract'])
    
    # Suggest related topics
    topics = agent.suggest_related_topics(paper['title'])
```


## Best Practices


1. **API Key Management**: Store your OpenAI API key securely in environment variables.
2. **Error Handling**: Implement proper error handling for API calls and tool operations.
3. **Context Management**: Use the context management features to maintain conversation coherence.
4. **Resource Cleanup**: Reset context and close connections when done.
5. **Logging**: Enable logging for debugging and monitoring.


## Notes

- Some features require additional dependencies
- Check documentation for specific requirements
- Monitor resource usage for large datasets
- Implement proper error recovery
- Keep tools updated for best performance
