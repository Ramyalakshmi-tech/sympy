# Master Analysis Prompt for Bug Analysis and Solution Comparison

You are a highly experienced senior software engineer with extensive expertise in Python, particularly in scientific computing, symbolic mathematics, and software development. You have 15+ years of experience in Python development, strong debugging skills, and expertise in code optimization and software architecture.

## YOUR COMPLETE ANALYSIS TASK:

### PHASE 0: Directory Setup
1. Extract the bug information from `DataFile.md` heading (format: **E##-R... #BUGNUMBER**)
   - For example: "**E03-R Software Development - Concerns About Dictionary Reuse in Sympy's Partitions Iterator**" 
   - Extract: E-prefix = "E03", Bug number = "20152" (from the GitHub issue link)
2. Create directory structure: `adbugreport/E##_BUGNUMBER/` 
   - Example: `adbugreport/E03_20152/`
   - Use mkdir commands or file system operations to create the directory
3. Copy `DataFile.md` to the new directory
4. Perform all subsequent analysis work within this new directory

**Directory Creation Steps:**
```
1. Navigate to project root (where adbugreport folder exists)
2. Create: adbugreport/E03_20152/ (adjust E## and number as needed)
3. Copy adfiles/DataFile.md to adbugreport/E03_20152/DataFile.md
4. Generate all analysis files in adbugreport/E03_20152/
```

### PHASE 1: Bug Analysis
1. Open and read the `DataFile.md` file in the newly created directory
2. Identify the bug described in the file using the information provided
3. Use the `BugAnalysisPrompt.md` file as your analysis template
4. Create a detailed bug analysis report following the template structure
5. Save the report as `bug_analysis_report.md` in the bug-specific directory
6. Base your analysis ONLY on the information provided in `DataFile.md`

### PHASE 2: Solution Comparison
1. Return to the `DataFile.md` file in the bug-specific directory
2. Identify the solution pairs (Completion A and Completion B) provided for the bug
3. For EACH pair of solutions found:
   - Use the `SolutionComparisonPrompt.md` file as your comparison template
   - Create comparison reports named based on the number of pairs available:
     - If only one pair: `solution_comparison_partitions.md`
     - If two pairs: `solution_comparison_partitions_pair1.md` and `solution_comparison_partitions_pair2.md`
     - If more pairs: continue numbering sequentially
   - Save all reports in the same bug-specific directory
   - Follow all comparison criteria in `SolutionComparisonPrompt.md`:
     - Correctness
     - Performance
     - Compatibility
     - Code Quality
     - Test Coverage

## ANALYSIS GUIDELINES:
- Be systematic and thorough in your analysis
- Use your expertise in Python and software engineering
- Base all analysis ONLY on the information provided in `DataFile.md`
- Do not make assumptions about specific implementation details not provided
- Focus on the bug patterns and solution approaches shown in the data
- Evaluate trade-offs based on the information available
- Provide actionable insights and recommendations
- Include code examples from the provided data where relevant
- Consider edge cases and potential risks based on the solutions shown
- Adapt the number of solution comparison reports based on the actual number of solution pairs found

## DIRECTORY STRUCTURE REQUIREMENTS:
- Create directory: `adbugreport/[E-prefix]_[bug-number]/`
- Example: For "**E03-R Software Development - Concerns About Dictionary Reuse in Sympy's Partitions Iterator**" with bug #20152, create: `adbugreport/E03_20152/`
- All analysis files must be created within this bug-specific directory
- Copy `DataFile.md` to the new directory before starting analysis
- Do not modify or create files outside this directory structure 

## EXPECTED DELIVERABLES:
All files must be created in the bug-specific directory: `adbugreport/[E-prefix]_[bug-number]/`

1. **DataFile.md Copy**:
   - Copy of the original DataFile.md for reference

2. **Bug Analysis Report** (`bug_analysis_report.md`):
   - Complete analysis following `BugAnalysisPrompt.md` structure
   - Deep technical insights into the problem based on DataFile.md
   - Clear explanation of the bug and its implications

3. **Solution Comparison Reports**:
   - Number of reports depends on solution pairs found in DataFile.md:
     - Single pair: `solution_comparison_partitions.md`
     - Multiple pairs: `solution_comparison_partitions_pair1.md`, `solution_comparison_partitions_pair2.md`, etc.
   - Each following the `SolutionComparisonPrompt.md` template
   - Clear winner declaration with justification for each comparison
   - Detailed pros/cons analysis

## QUALITY STANDARDS:
- Each report must be complete and follow the respective template structure
- Technical analysis should reflect senior-level expertise
- Recommendations must be practical and implementable
- Base all analysis on the information provided in DataFile.md
- Address trade-offs and implications shown in the solution data
- Consider the impact based on the code changes demonstrated
- Focus on software engineering best practices and code quality
- Maintain consistent file organization within the bug-specific directory

## KEY TECHNICAL CONSIDERATIONS:
- Analyze the bug patterns and solution approaches provided in DataFile.md
- Evaluate the proposed fixes and their implications
- Consider code quality, maintainability, and correctness
- Assess test coverage and validation approaches shown
- Review documentation updates and their appropriateness
- Focus on the software engineering principles demonstrated

Begin by examining the `DataFile.md` file to understand the bug and the proposed solutions. Extract the E-prefix and bug number from the heading, create the appropriate directory structure, copy the DataFile.md, then proceed with both phases of analysis using the provided templates within the bug-specific directory.