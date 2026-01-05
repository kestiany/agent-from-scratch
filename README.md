# agent-from-scratch

This repository documents my learning journey of building an AI Agent
from first principles.

The goal is not to create a production-ready framework, but to deeply
understand what an Agent really is beyond prompts — including its state,
control flow, and execution loop.

---

## Motivation

Most Agent tutorials focus on *what* an Agent can do.
This project focuses on *how* an Agent works internally.

I want to answer questions like:
- What is the minimal runtime of an Agent?
- How should Agent state be modeled?
- How does planning, execution, and evaluation form a controllable loop?

---

## Scope

**This repository is:**
- A personal learning and exploration project
- A public build of my understanding
- Focused on clarity over completeness

**This repository is NOT:**
- A production framework
- A collection of prompt tricks
- An optimized or benchmark-driven project

---

## Current Capabilities

As of Week 1, this project includes:
- A minimal Agent runtime loop (think / act / evaluate)
- An explicit AgentState as the single source of truth
- Step-based control flow with termination conditions
- A runnable example demonstrating the full loop

What it does NOT include yet:
- Tool calling
- External memory / RAG
- Multi-agent coordination
- Performance optimizations

---

## How to Read This Repository

If this is your first time here:

1. Start with **Week 1 design notes**  
   → [`docs/week01-design.md`](docs/week01-design.md)

2. Look at the core runtime:
   - [`AgentState`](src/agent/state.py)
   - [`AgentKernel`](src/agent/kernel.py)

3. Run the minimal example:
   ```bash
   python src/main.py
