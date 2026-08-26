# Code Review Task

Perform a comprehensive code review using:

- The custom code review agent.
- Repository code review instructions.
- Requirements and user stories.
- Acceptance criteria.
- HLD / LLD / design documents.
- Relevant source code.
- Relevant tests.
- Coding standards.
- Security guidelines when available.
- Static-analysis findings when supplied.

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
| Architecture Compliance | Pass / Partial / Fail | |
| Coding Standards | Pass / Partial / Fail | |
| Security | Pass / Partial / Fail | |
| Performance | Pass / Partial / Fail | |
| Reliability | Pass / Partial / Fail | |
| Test Coverage | Pass / Partial / Fail | |

## Critical Findings

## Major Findings

## Minor Findings

## Static Analysis Findings Review

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
