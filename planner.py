import json
from llm import call_llm

SYSTEM_PROMPT = """
You are a research planner.

RULES:
- You MUST return valid JSON
- You MUST include BOTH keys:
  - "subquestions"
  - "search_keywords"
- Values must be arrays of strings
- Do NOT omit keys
- Do NOT add extra keys
"""

def plan_research(question):
    response = call_llm(
        SYSTEM_PROMPT,
        f"""
Research question: {question}

Return JSON exactly in this format:
{{
  "subquestions": ["..."],
  "search_keywords": ["..."]
}}
"""
    )
    return json.loads(response)
