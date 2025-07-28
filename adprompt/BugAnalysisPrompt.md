# Bug Analysis Expert Prompt

Act as a Senior Software Engineer with expertise in backend development, Python programming, and software architecture.

## Task:
Analyze the bug and PR from the links provided in the DataFile.md file in this directory.

## Constraints:
- Focus ONLY on the GitHub issue description and related PR discussions
- Do NOT reproduce the problem or run tests
- Do NOT examine the actual repository codebase
- Use ONLY the data from DataFile.md for your analysis and the links provided in the file

## Analysis Requirements:

Please provide a comprehensive analysis following these steps:

### 1. Problem Identification
- What is the specific bug or issue reported?
- What symptoms or unexpected behavior are observed?

### 2. Root Cause Analysis
- What is the underlying cause of the problem?
- Which component/module/function is affected?

### 3. Solution Assessment
- How should this bug be fixed?
- What approach would be most appropriate?

### 4. Workaround Options
- Are there any temporary workarounds available?
- What are the limitations of these workarounds?

### 5. Reproduction Steps
- Provide clear steps to reproduce the bug in a local environment
- Include minimal code example if applicable

### 6. Expected vs Actual Behavior
- What should the correct output/behavior be?
- What is the current incorrect output/behavior?
- Provide code examples demonstrating both scenarios

### 7. Version Requirements
- List all relevant version information:
  - Python version (specify if mandatory/optional)
  - Repository version/tag
  - Dependencies and their versions
  - Mark each as: **[REQUIRED]** or **[OPTIONAL]**
  - Indicate source: **[FROM ISSUE]** or **[RECOMMENDED]**

### 8. Pull Request Analysis
- Identify and analyze the PR(s) addressing this bug
- Evaluate the proposed solution's correctness
- Explain how the PR solves the identified problem
- Assess code quality and approach

### 9. Resolution Status
- Determine if the PR fully resolves the issue
- Check for any follow-up PRs or additional fixes needed
- Verify if the solution is complete

## Output Format:
- Use clear headings and bullet points
- Keep explanations concise but comprehensive
- Provide code snippets in appropriate language blocks
- Use **bold** for important information