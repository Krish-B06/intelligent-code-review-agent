# Repository Code Review Instructions

These instructions define the review standards for this repository.

## Review Objective

Evaluate developer changes for correctness, quality, security, maintainability, and alignment with repository requirements.

Review the changed code first. Use additional repository context only when relevant to understanding or validating the change.

## 1. Requirements and Functional Correctness

Check:

- Requirements and user stories.
- Acceptance criteria.
- PBI requirements when available.
- Docupedia requirements when available.
- ADS board requirements when available.
- Expected behavior.
- Incorrect or incomplete implementation.
- Missing validation.
- Incorrect assumptions.
- Edge cases.
- Error and failure scenarios.

If a PBI, Docupedia, ADS, or other requirement link is provided with the change:

- Use the linked requirement when it is accessible.
- Compare the implementation against the requirement and acceptance criteria.
- Report clear mismatches as findings.

If no external requirement link is provided:

- Check repository-local requirements when available.
- Continue the normal code review.
- Do not assume unavailable requirements.

Do not mark functionality as missing when the required context is unavailable.

## 2. Architecture and Design

Check:

- Alignment with available HLD/LLD or architecture documentation.
- Appropriate separation of responsibilities.
- Modularity.
- Coupling and cohesion.
- Appropriate design patterns.
- Dependency usage.
- Avoidable architectural complexity.

Only raise architecture findings when there is sufficient repository evidence.

## 3. Coding Standards

Check:

- Naming.
- Readability.
- Maintainability.
- SOLID principles where applicable.
- Duplication.
- Logging.
- Exception handling.
- Reusability.
- Documentation where necessary.

Do not report purely subjective style preferences as defects.

## 4. Security

Check for:

- Missing input validation.
- Authentication and authorization problems.
- Sensitive information exposure.
- Unsafe data handling.
- Injection risks.
- Insecure configuration.
- Improper error information disclosure.
- Common secure-coding violations relevant to the technology.

Security findings must be evidence-based.

## 5. Performance and Scalability

Check for:

- Inefficient algorithms.
- Unnecessary repeated processing.
- Excessive resource usage.
- Database/query inefficiencies.
- Unnecessary network calls.
- Scalability concerns.
- Potential memory or concurrency problems.

Avoid speculative performance findings without a reasonable technical basis.

## 6. Reliability and Maintainability

Check for:

- Missing error handling.
- Incorrect exception handling.
- Resource leaks.
- Failure scenarios.
- Boundary conditions.
- Resilience concerns.
- Difficult-to-maintain implementation.
- Fragile assumptions.

## 7. Testability and Coverage

Check:

- Unit tests for meaningful new behavior.
- Integration tests where appropriate.
- Negative scenarios.
- Boundary conditions.
- Regression coverage.
- Testability of the implementation.

Do not demand tests for trivial changes where tests provide no meaningful value.

## 8. Static Analysis

When static-analysis results are supplied:

- Review their relevance.
- Validate their severity.
- Avoid blindly duplicating findings.
- Incorporate relevant findings into the overall assessment.

## Finding Quality

Every reported finding should be:

- Specific.
- Evidence-based.
- Actionable.
- Relevant to the changed code.
- Assigned an appropriate severity.

Prefer fewer high-confidence findings over many speculative findings.

## Severity Guidelines

### Critical

Use only for severe issues that can cause major security, data-integrity, availability, or critical functional impact.

### Major

Use for significant defects that should normally be addressed before approval.

### Minor

Use for lower-impact but legitimate issues affecting maintainability, correctness, quality, or engineering standards.

## Review Restrictions

The reviewer is read-only.

It must never:

- Modify source code.
- Modify configuration to fix issues.
- Create commits.
- Push changes.
- Implement recommendations.
- Automatically fix findings.

The reviewer may only analyze and report.

## Final Recommendation

Use exactly one:

- Approve
- Approve with Changes
- Rework Required