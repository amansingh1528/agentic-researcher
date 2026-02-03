# Agentic Research AI

## Overview

This project implements a research-focused **Agentic AI system** that autonomously plans, searches, reads, synthesizes, and critically evaluates scientific information to answer a research question without hallucinating.

The system is intentionally conservative: if sufficient evidence is not found, it explicitly reports **"insufficient data"** instead of fabricating content.

The entire system runs locally, free of cost, on CPU-only hardware using open-source language models.

---

## Primary Goal

The goal of this AI is to behave like a careful junior researcher. It looks up relevant research papers, extracts only factual information, summarizes what is supported by evidence, and refuses to guess when information is missing.

---

## Why This Is Agentic AI

This project is classified as **Agentic AI** because it demonstrates autonomous goal-directed behavior:

- It plans how to approach a research question
- It executes multiple actions without human intervention
- It evaluates its own output
- It decides whether an answer is trustworthy enough to release
- It stores intermediate results as memory

A simple AI agent answers questions. This system reasons about how to answer them and whether it should answer at all.

---

## System Architecture

Research Question  
→ Planner (strategy generation)  
→ Searcher (paper discovery)  
→ Reader (fact extraction)  
→ Synthesizer (structured aggregation)  
→ Critic (hallucination prevention)  
→ Final Output or Rejection

---

## Project Structure

```text
research_agent/
├── agent.py              # Main orchestrator
├── planner.py            # Research planning logic
├── searcher.py           # Paper retrieval
├── reader.py             # Fact extraction
├── synthesizer.py        # Fact synthesis
├── critic.py             # Output validation
├── llm.py                # Local LLM interface
├── memory/               # Persistent agent memory
│   ├── notes.json
│   ├── sources.json
│   ├── synthesis_raw.txt
│   └── final_report.json
└── README.md
```

## Component Responsibilities

Planner  
Transforms a research question into structured search keywords. Retries until a valid plan is produced.

Searcher  
Finds a bounded number of relevant research papers based on planner output.

Reader  
Extracts factual claims from papers and associates them with sources. Papers that fail extraction are skipped.

Synthesizer  
Combines extracted facts into structured research insights while enforcing strict JSON output.

Critic  
Validates the synthesized output. Accepts the result if at least one section contains supported claims and marks missing sections as "insufficient data". Rejects output if no supported claims exist.

Agent (Orchestrator)  
Coordinates all steps, enforces validation, handles retries, and saves final approved output.

---

### Non-Hallucination Guarantee

The system enforces the following rules:
- No unsupported claims are allowed
- No missing data is guessed
- All incomplete sections are explicitly labeled
- Output is rejected if evidence is insufficient

This design prioritizes correctness over completeness.

---

## Installation

### Environment Setup

    conda create -n research-agent python=3.11
    conda activate research-agent

### Dependencies

    pip install requests tqdm

### Local LLM Setup

Download Ollama from:
https://ollama.com/download

### Pull a free model:

    ollama pull llama3

---

### Running the Project

    python agent.py

### The final validated output will be saved to:

    memory/final_report.json

---

## Hardware Requirements
- CPU only
- No GPU required
- No paid APIs
- No cloud services

---

## Design Trade-offs
- The system may return partial outputs
- Some sections may report "insufficient data"
- The agent prefers silence over speculation

These trade-offs are intentional and ensure trustworthiness.

---

## License

Open-source and intended for educational and research use.

---

## Author
Aman Singh Chauhan
