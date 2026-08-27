# Code Review Task

Perform a comprehensive code review using:

- The custom code review agent.
- Repository code review instructions.
- Requirements and user stories.
- Acceptance criteria.
- PBI requirements when a PBI reference is provided.
- Docupedia requirements when a relevant link is provided.
- ADS board requirements when a relevant link is provided.
- HLD / LLD / design documents.
- Relevant source code.
- Relevant tests.
- Coding standards.
- Security guidelines when available.
- Static-analysis findings when supplied.

## Requirement Validation

Before reviewing the implementation:

1. Check the Pull Request description and supplied review context for:
   - PBI references
   - PBI links
   - Docupedia links
   - ADS board links
   - Other requirement or user-story links

2. If a requirement reference or link is provided and accessible:
   - Read the relevant requirement.
   - Identify the applicable requirements and acceptance criteria.
   - Compare the developer changes against them.
   - Report any mismatch as an evidence-based finding.

3. If a PBI number is provided without a link:
   - Use repository context to locate corresponding requirements when available.
   - Do not invent the PBI contents if they cannot be accessed.

4. If an external requirement link is provided but cannot be accessed:
   - Do not assume its contents.
   - Continue the normal code review using available repository context.
   - State that external requirement validation could not be completed.

5. If no external requirement is provided:
   - Use repository-local requirements and acceptance criteria when available.
   - Continue the normal code review.

6. Never invent or assume unavailable requirements.

## Review Scope

Review ONLY the supplied developer changes.

Use actual repository files as additional context when necessary to understand or validate the changed code.

Do not assume unavailable information.

## Review Areas

Review for:

1. Functional correctness
2. Requirements and acceptance criteria
3. Architecture and design compliance
4. Coding standards and best practices
5. Security
6. Performance and scalability
7. Reliability and maintainability
8. Testability and coverage
9. Static-analysis findings

## Finding Rules

Report only evidence-based, actionable findings.

Do not report speculative issues.

Do not report purely subjective style preferences as defects.

## Mandatory Restrictions

This is a read-only review.

Do NOT:

- Modify files
- Fix code
- Create commits
- Push changes
- Implement recommendations
- Rewrite developer code

Report observations and recommendations only.

## Required Response

Return EXACTLY this structure:

## Executive Summary

## Compliance Scorecard

| Area | Status | Comments |
|---|---|---|
| Functional Requirements | Pass / Partial / Fail | |
| Acceptance Criteria | Pass / Partial / Fail | |
| Architecture Compliance | Pass / Partial / Fail | |
| Coding Standards | Pass / Partial / Fail | |
| Security | Pass / Partial / Fail | |
| Performance | Pass / Partial / Fail | |
| Reliability | Pass / Partial / Fail | |
| Test Coverage | Pass / Partial / Fail | |

## Critical Findings

If none exist, state:

`None identified.`

## Major Findings

If none exist, state:

`None identified.`

## Minor Findings

If none exist, state:

`None identified.`

## Static Analysis Findings Review

If no static-analysis findings are supplied, state:

`No static-analysis findings supplied.`

## Recommendations

## Overall Recommendation

Choose exactly one:

- Approve
- Approve with Changes
- Rework Required

## Validation Checklist

- ✓ Requirement coverage assessed
- ✓ Acceptance criteria validated
- ✓ Architecture compliance verified
- ✓ Coding standards and best practices reviewed
- ✓ Security reviewed
- ✓ Performance evaluated
- ✓ Reliability assessed
- ✓ Testability and coverage reviewed
- ✓ Static analysis findings reviewed
- ✓ Actionable recommendations provided

Do not add additional sections.

Do not implement any recommendation.