# Intelligent Code Review Agent

A repository-contained AI code review solution with two review modes:

1. **Repository/Server Reviewer** – Automatically reviews developer changes when a Pull Request is created or updated.
2. **Local Reviewer** – Allows developers to manually review their changes during development before creating a Pull Request.

## Code Review Modes

### 1. Repository/Server Reviewer

The repository reviewer runs automatically through GitHub Actions.

It is triggered when:

- A Pull Request is created.
- A Pull Request is updated.
- The workflow is manually triggered when required.

The reviewer analyzes the developer's changes and posts the review result to the Pull Request.

The review is read-only and does not:

- Modify source code
- Create correction commits
- Push changes
- Implement recommendations

### 2. Local Code Reviewer

Developers can run the local reviewer during development before creating a Pull Request.

Run:

```bash
./scripts/local-code-review.sh main
The reviewer compares the current branch against main and analyzes the changes using the repository's:

Code review agent
Review instructions
Review prompt
Requirements and acceptance criteria
Relevant source-code context
Relevant tests
Architecture/design documentation when available
Static-analysis findings when available

The reviewer evaluates:

Functional correctness
Requirements compliance
Architecture and design
Coding standards and maintainability
Security
Performance and scalability
Reliability
Testability and coverage
Static-analysis findings

The local reviewer is read-only. It does not modify files, create commits, push changes, or implement fixes.

The generated review is stored locally at:

review-output/local-review.md

The review-output/ directory is ignored by Git, so the local review remains available only to the developer unless they explicitly share it.

Recommended Developer Workflow

Create or switch to your feature branch:

git checkout -b feature/my-change

Make your code changes.

Run the local code review:

./scripts/local-code-review.sh main

View the generated review:

cat review-output/local-review.md

Address the findings if required.

Then commit and push your changes:

git add .
git commit -m "Describe your changes"
git push

Create or update the Pull Request.

The repository/server reviewer will then automatically review the Pull Request.

Review Output

The review contains:

Executive Summary
Compliance Scorecard
Critical Findings
Major Findings
Minor Findings
Static Analysis Findings Review
Recommendations
Overall Recommendation
Validation Checklist

Each finding includes relevant evidence, location, impact, and recommended action.

Repository Structure
.github/
├── agents/
│   └── code-review.agent.md
├── instructions/
│   └── code-review.instructions.md
├── prompts/
│   └── code-review.prompt.md
└── workflows/
    └── code-review.yml

scripts/
└── local-code-review.sh

src/
    # Project source code

tests/
    # Project tests

requirements/
    # Project requirements and acceptance criteria
Important

The code review agent is intended to identify and report issues only.

It must never automatically:

Modify developer code
Fix findings
Create commits
Push changes
Implement recommendations