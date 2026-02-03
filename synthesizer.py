'''import json
from llm import call_llm

SYSTEM_PROMPT = """
You are a research synthesizer.
ONLY use provided facts.
Do NOT introduce new claims.
Cite sources for every claim.
"""

def synthesize(facts):
    response = call_llm(
        SYSTEM_PROMPT,
        f"Facts:\n{json.dumps(facts, indent=2)}"
    )
    return json.loads(response)
'''
import json
import re
from llm import call_llm

SYSTEM_PROMPT = """
You are a research synthesizer.

STRICT RULES:
- You MUST return valid JSON only
- Do NOT include explanations, markdown, or comments
- Use double quotes for all keys and strings
- Do NOT invent new facts
- ONLY use the provided facts
- Every claim must reference a source paper title

Return JSON in EXACTLY this format:
{
  "trends": [],
  "common_methods": [],
  "datasets": [],
  "open_problems": []
}
"""

def _extract_json(text):
    """
    Extract the first valid JSON object from text.
    This protects against accidental extra text.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM response")
    return match.group(0)

def synthesize(facts):
    response = call_llm(
        SYSTEM_PROMPT,
        f"FACTS:\n{json.dumps(facts, indent=2)}"
    )

    # Save raw response for debugging
    with open("memory/synthesis_raw.txt", "w") as f:
        f.write(response)

    try:
        json_text = _extract_json(response)
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(
            "Synthesizer returned invalid JSON.\n"
            "Raw output saved to memory/synthesis_raw.txt"
        ) from e
