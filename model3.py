# Import required libraries
import os
from groq import Groq # Import Groq API client
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

# Retrieve API key from environment variables(.env should contain the api key with GROQ_API name)
api_key = os.getenv("GROQ_API")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY environment variable is not set.")

# Initialize the Groq API client
client = Groq(api_key=api_key)

def generate_career_recommendations(name, skills, interests):
    """
    Generate career recommendations using Groq AI (model:Llama3).
    
    Parameters:
    - name (str): User's name
    - skills (str): User's skills (comma-separated)
    - interests (str): User's interests (comma-separated)
    
    Returns:
    - str: Top 3 career recommendations based on skills and interests
    """
    # Define the prompt for the AI model
    prompt = f"My name is {name}. My skills are {skills}. I am interested in {interests}. What are the best 3 career options for me?"
    
    try:
        # Generate a response using the AI model
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a career advisor. Provide the top 3 best career paths based on the user's skills and interests."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the generated career suggestions
        suggestions = response.choices[0].message.content
        return suggestions
    
    except Exception as e:
        return f"An error occurred: {e}"

def generate_learning_path(career):
    """
    Generate a structured learning path for the selected career.
    
    Parameters:
    - career (str): The chosen career field
    
    Returns:
    - str: A step-by-step learning path with essential skills, courses, and resources
    """
    # Define the prompt for the AI model
    prompt = f"I want to become a {career}. Provide a step-by-step learning path, including essential skills, online courses, and resources."

    try:
        # Generate a response using the AI model
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a career mentor. Provide a structured learning roadmap for the given career."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the generated learning path
        path = response.choices[0].message.content
        return path
    
    except Exception as e:
        return f"An error occurred: {e}"
