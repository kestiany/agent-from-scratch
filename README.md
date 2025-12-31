# agent-from-scratch

This repository documents my learning journey of building an AI Agent
from first principles.

The goal is not to create a production-ready framework, but to deeply
understand what an Agent really is beyond prompts — including its state,
control flow, and execution loop.

## Motivation

Most Agent tutorials focus on *what* an Agent can do.
This project focuses on *how* an Agent works internally.

I want to answer questions like:
- What is the minimal runtime of an Agent?
- How should Agent state be modeled?
- How does planning, execution, and evaluation form a controllable loop?

## Scope

**This repository is:**
- A personal learning and exploration project
- A public build of my understanding
- Focused on clarity over completeness

**This repository is NOT:**
- A production framework
- A collection of prompt tricks
- An optimized or benchmark-driven project

## Project Structure

```text
agent-from-scratch/
├── docs/          # design notes & daily thinking logs
├── src/           # agent runtime implementation
├── examples/      # minimal runnable examples
└── tests/         # tests (added gradually)
