"""
Basic usage examples for SolentraAgent
"""
from solentra import SolentraAgent
from solentra.tools import MLTools, DataTools, ResearchTools
import numpy as np
import pandas as pd

def basic_agent_usage():
    """Demonstrate basic agent initialization and usage."""
    # Initialize agent with default settings
    agent = SolentraAgent(
        agent_name="Research Scientist",
        model_name="solentra-70b",
        tools_enabled=True
    )
    
    # Generate a response
    response = agent.generate_response(
        "Explain the concept of quantum tunneling in enzyme catalysis"
    )
    print("Response:", response)
    
    # Create an experiment protocol
    protocol = agent.create_experiment(
        steps=["Sample preparation", "Data collection"],
        materials=["Reagent A", "Equipment B"],
        duration="2 hours",
        conditions={"temperature": 25}
    )
    print("\nExperiment Protocol:", protocol)
    
    # Run the experiment
    results = agent.run_experiment(
        protocol=protocol,
        variables={"concentration": 0.5},
        iterations=3
    )
    print("\nExperiment Results:", results)
    
    # Analyze data
    data = [1.2, 1.3, 1.1, 1.4, 1.2]
    analysis = agent.analyze_data(data, confidence_level=0.95)
    print("\nData Analysis:", analysis)

def persona_examples():
    """Demonstrate different agent personas."""
    # Create a physicist agent
    physicist = SolentraAgent(
        persona="physicist",
        temperature=0.7,
        max_tokens=200
    )
    
    # Create a biologist agent
    biologist = SolentraAgent(
        persona="biologist",
        temperature=0.7,
        max_tokens=200
    )
    
    # Get responses from different personas
    physics_response = physicist.generate_response(
        "Explain quantum tunneling in enzymes"
    )
    print("\nPhysicist's Response:", physics_response)
    
    biology_response = biologist.generate_response(
        "Explain quantum tunneling in enzymes"
    )
    print("\nBiologist's Response:", biology_response)

def context_management():
    """Demonstrate context management features."""
    agent = SolentraAgent(use_context=True)
    
    # Learn and recall information
    agent.learn("quantum_tunneling", "A quantum mechanical phenomenon where particles can pass through potential barriers")
    recalled = agent.recall("quantum_tunneling")
    print("\nRecalled Information:", recalled)
    
    # Summarize text
    text = "Quantum tunneling is a fundamental quantum mechanical phenomenon where particles can pass through potential barriers that would be classically forbidden. This effect is particularly important in enzyme catalysis, where it allows for more efficient chemical reactions."
    summary = agent.summarize(text)
    print("\nSummary:", summary)
    
    # Extract key points
    key_points = agent.extract_key_points(text)
    print("\nKey Points:", key_points)
    
    # Suggest related topics
    topics = agent.suggest_related_topics("quantum tunneling")
    print("\nRelated Topics:", topics)

def main():
    print("=== Basic Agent Usage ===")
    basic_agent_usage()
    
    print("\n=== Persona Examples ===")
    persona_examples()
    
    print("\n=== Context Management ===")
    context_management()

if __name__ == "__main__":
    main()
