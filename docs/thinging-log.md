### Week 1

- Decision: Use a single AgentState as the only shared state
- Reason: Avoid hidden state and improve debuggability
- Open Question: How this state should evolve with parallel steps is unclear

- Decision: Keep evaluation simple (only completion check)
- Reason: Focus on control flow first
- Open Question: How to represent partial failure or low-quality results
