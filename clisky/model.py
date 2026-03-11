from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


system = """
You are a cli command recommendation tool.
You will be given a prompt from the user and you will recommend a CLI command.

Rules:
- Only output the command
- Do not explain anything
- Do not add extra text
- Commands must be Linux based
- If multiple commands are needed separate them with ";"
- If you cannot determine the command return exactly: I don't know
"""

def cli_recommend(prompt):
    print("prompt:", prompt)

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0.1,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": f"This is my prompt:\n{prompt}"}
        ],
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print(cli_recommend("install python"))