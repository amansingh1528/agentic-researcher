import subprocess
import json

MODEL = "llama3"

def call_llm(system_prompt, user_prompt):
    prompt = f"""
SYSTEM:
{system_prompt}

USER:
{user_prompt}

Respond ONLY in valid JSON.
"""
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
