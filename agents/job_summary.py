from apimyllama import ApiMyLlama
import requests

# Replace with your actual values
OLLAMA_SERVER_IP = "localhost"
OLLAMA_SERVER_PORT = "3001"
OLLAMA_API_KEY = "80ad9712b6b7877d770d2d5e89f34612441d3940"  # Replace this with your key
MODEL = "mistral"

api = ApiMyLlama(OLLAMA_SERVER_IP, OLLAMA_SERVER_PORT)

def generate_summary_with_ollama(title, description):
    prompt = f"""
You are an AI assistant that extracts structured information from job descriptions.

Given the following Job Title and Job Description, extract the key details and provide them in the following format:

Job Title: <title>
Responsibilities: <bullet points>
Skills Required: <bullet points or comma-separated list>
Experience: <summary of experience requirements>
Qualifications: <summary of education/certifications needed>
Job Summary: <3–5 line concise summary of the job>

Job Title: {title}
Job Description: {description}
"""
    try:
        result = api.generate(OLLAMA_API_KEY, prompt, MODEL)
        return result
    except requests.RequestException as e:
        return f"Error generating summary: {e}"
