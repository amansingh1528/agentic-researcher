'''import json
from planner import plan_research
from searcher import search_papers
from reader import extract_facts
from synthesizer import synthesize
from critic import review

# ==========================
# CONFIG
# ==========================
QUESTION = "Recent surrogate modeling methods for DrivAERnet++"
MAX_PLANNER_RETRIES = 3
MAX_PAPERS = 5

# ==========================
# STEP 1: PLANNER (with retries)
# ==========================
plan = None

for attempt in range(MAX_PLANNER_RETRIES):
    print(f"\n[Planner] Attempt {attempt + 1}")
    try:
        plan = plan_research(QUESTION)

        # ---- VALIDATION ----
        if not isinstance(plan, dict):
            raise ValueError("Planner output is not a dictionary")

        if "search_keywords" not in plan:
            raise ValueError("Missing 'search_keywords'")

        if not isinstance(plan["search_keywords"], list):
            raise ValueError("'search_keywords' is not a list")

        if len(plan["search_keywords"]) == 0:
            raise ValueError("'search_keywords' is empty")

        print("[Planner] Success")
        break

    except Exception as e:
        print(f"[Planner] Failed: {e}")
        plan = None

if plan is None:
    raise RuntimeError("Planner failed after maximum retries")

print("\nPlanner Output:")
print(json.dumps(plan, indent=2))

# ==========================
# STEP 2: SEARCH
# ==========================
print("\n[Search] Fetching papers...")
papers = search_papers(plan["search_keywords"], max_results=MAX_PAPERS)

if not papers:
    raise RuntimeError("No papers found. Cannot continue.")

print(f"[Search] Found {len(papers)} papers")

# ==========================
# STEP 3: READER (FACT EXTRACTION)
# ==========================
print("\n[Reader] Extracting facts...")
facts = []

for idx, paper in enumerate(papers, 1):
    print(f"  Reading paper {idx}: {paper['title']}")
    try:
        extracted = extract_facts(paper)
        facts.append(extracted)
    except Exception as e:
        print(f"  Skipped paper due to error: {e}")

if not facts:
    raise RuntimeError("No valid facts extracted")

print(f"[Reader] Extracted facts from {len(facts)} papers")

# ==========================
# STEP 4: SYNTHESIS
# ==========================
print("\n[Synthesizer] Synthesizing research...")
synthesis = synthesize(facts)

print("\nSYNTHESIS OUTPUT:")
print(json.dumps(synthesis, indent=2))

# ==========================
# STEP 5: CRITIC (HALLUCINATION CHECK)
# ==========================
print("\n[Critic] Reviewing synthesis...")
verdict = review(synthesis, facts)

print("\nCRITIC VERDICT:")
print(json.dumps(verdict, indent=2))

# ==========================
# STEP 6: FINAL DECISION
# ==========================
if verdict.get("status") == "PASS":
    print("\nFINAL RESEARCH OUTPUT (APPROVED)")
    print(json.dumps(synthesis, indent=2))

    # Optional: save output
    with open("memory/final_report.json", "w") as f:
        json.dump(synthesis, f, indent=2)

else:
    print("\nOUTPUT REJECTED BY CRITIC")
    print("Issues:")
    for issue in verdict.get("issues", []):
        print("-", issue)
'''
import json
from planner import plan_research
from searcher import search_papers
from reader import extract_facts
from synthesizer import synthesize
from critic import critique

# ==========================
# CONFIG
# ==========================
QUESTION = "Recent surrogate modeling methods for DrivAERnet++"
MAX_PLANNER_RETRIES = 3
MAX_PAPERS = 5

# ==========================
# STEP 1: PLANNER (with retries)
# ==========================
plan = None

for attempt in range(MAX_PLANNER_RETRIES):
    print(f"\n[Planner] Attempt {attempt + 1}")
    try:
        plan = plan_research(QUESTION)

        # ---- VALIDATION ----
        if not isinstance(plan, dict):
            raise ValueError("Planner output is not a dictionary")

        if "search_keywords" not in plan:
            raise ValueError("Missing 'search_keywords'")

        if not isinstance(plan["search_keywords"], list):
            raise ValueError("'search_keywords' is not a list")

        if len(plan["search_keywords"]) == 0:
            raise ValueError("'search_keywords' is empty")

        print("[Planner] Success")
        break

    except Exception as e:
        print(f"[Planner] Failed: {e}")
        plan = None

if plan is None:
    raise RuntimeError("Planner failed after maximum retries")

print("\nPlanner Output:")
print(json.dumps(plan, indent=2))

# ==========================
# STEP 2: SEARCH
# ==========================
print("\n[Search] Fetching papers...")
papers = search_papers(plan["search_keywords"], max_results=MAX_PAPERS)

if not papers:
    raise RuntimeError("No papers found. Cannot continue.")

print(f"[Search] Found {len(papers)} papers")

# ==========================
# STEP 3: READER (FACT EXTRACTION)
# ==========================
print("\n[Reader] Extracting facts...")
facts = []

for idx, paper in enumerate(papers, 1):
    print(f"  Reading paper {idx}: {paper['title']}")
    try:
        extracted = extract_facts(paper)
        facts.append(extracted)
    except Exception as e:
        print(f"  Skipped paper due to error: {e}")

if not facts:
    raise RuntimeError("No valid facts extracted")

print(f"[Reader] Extracted facts from {len(facts)} papers")

# ==========================
# STEP 4: SYNTHESIS
# ==========================
print("\n[Synthesizer] Synthesizing research...")
synthesis = synthesize(facts)

print("\nRAW SYNTHESIS OUTPUT:")
print(json.dumps(synthesis, indent=2))

# ==========================
# STEP 5: CRITIC
# ==========================
print("\n[Critic] Reviewing synthesis...")
accepted, reviewed_synthesis = critique(synthesis)

# ==========================
# STEP 6: FINAL DECISION
# ==========================
if accepted:
    print("\nFINAL RESEARCH OUTPUT (APPROVED)")
    print(json.dumps(reviewed_synthesis, indent=2))

    with open("memory/final_report.json", "w") as f:
        json.dump(reviewed_synthesis, f, indent=2)

else:
    print("\nOUTPUT REJECTED BY CRITIC")
    print("Reason: No section contained sufficient supported data.")

