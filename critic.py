'''import json
from llm import call_llm

SYSTEM_PROMPT = """
You are a strict reviewer.
Reject any claim without explicit source support.
"""

def review(synthesis, facts):
    response = call_llm(
        SYSTEM_PROMPT,
        f"""
Synthesis:
{json.dumps(synthesis, indent=2)}

Facts:
{json.dumps(facts, indent=2)}

Check for unsupported claims.
"""
    )
    return json.loads(response)
'''
def critique(synthesis):
    """
    Critic rules:
    - Accept if at least one section has at least one item
    - Do NOT invent content
    - Mark empty sections as 'insufficient data'
    """

    REQUIRED_SECTIONS = [
        "trends",
        "common_methods",
        "datasets",
        "open_problems",
    ]

    accepted = False

    for section in REQUIRED_SECTIONS:
        # If section missing or empty → mark insufficient data
        if section not in synthesis or not synthesis[section]:
            synthesis[section] = ["insufficient data"]
        else:
            # At least one real claim exists
            accepted = True

    if not accepted:
        return False, None

    return True, synthesis
