import json
from llm import call_llm

SYSTEM_PROMPT = """
You are a paper reader.
Extract ONLY information explicitly stated.
If information is missing, write "NOT FOUND".
"""

def extract_facts(paper):
    response = call_llm(
        SYSTEM_PROMPT,
        f"""
Paper title: {paper['title']}
Abstract: {paper['summary']}

Extract:
- problem
- method
- data
- results
- limitations
"""
    )
    facts = json.loads(response)
    facts["source"] = paper["title"]
    return facts
