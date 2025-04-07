import openai
import os

# Load your OpenAI API key from environment variable
openai.api_key = os.getenv("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")

def generate_summary_with_openai(title, description):
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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.5
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating summary: {e}"
