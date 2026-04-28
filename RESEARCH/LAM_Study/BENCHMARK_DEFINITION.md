# LAM Benchmark Definition

## Objective
To measure the ability of a model to achieve a complex goal in a non-textual environment through a sequence of discrete action tokens.

## Environment Candidates
1. **Web Browser (Playwright/Selenium):** High complexity, high dimensionality.
2. **OS Interface (GUI):** Extremely high dimensionality.
3. **Code Execution (REPL/Bash):** Controlled, discrete, high feedback density.

## Metrics
- **Success Rate (SR):** % of goals achieved.
- **Step Efficiency (SE):** Ratio of optimal steps to actual steps taken.
- **Recovery Rate (RR):** Ability to correct course after an error signal from the environment.
