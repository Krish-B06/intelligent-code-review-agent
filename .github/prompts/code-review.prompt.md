# Code Review Task

Review the supplied developer changes using:

- The custom code review agent instructions.
- The repository code review instructions.
- Supplied requirements and acceptance criteria.
- Relevant architecture/design documentation.
- Relevant tests.
- Supplied static-analysis results.

## Review Context

The review input may contain:

- Changed files.
- Git diff.
- Relevant surrounding source code.
- Requirements or user story.
- Acceptance criteria.
- Architecture/design documentation.
- Relevant tests.
- Static-analysis results.

Review only the supplied change and the context necessary to understand it.

Do not assume unavailable information.

## Required Response

### Executive Summary

Provide a concise assessment of the change.

### Compliance Scorecard

| Area | Status | Comments |
|---|---|---|
| Functional Requirements | Pass / Partial / Fail | |
| Architecture Compliance | Pass / Partial / Fail | |
| Coding Standards | Pass / Partial / Fail | |
| Security | Pass / Partial / Fail | |
| Performance | Pass / Partial / Fail | |
| Reliability | Pass / Partial / Fail | |
| Test Coverage | Pass / Partial / Fail | |

### Findings

Group findings into:

#### Critical

List only high-confidence critical findings.

#### Major

List significant findings that should normally be addressed before approval.

#### Minor

List legitimate lower-impact findings.

For each finding, provide:

- Severity
- File and line
- Observation
- Why it matters
- Recommended action

If a severity category has no findings, state:

`None identified.`

### Recommendations

Provide additional recommendations that are useful but do not represent findings.

Do not implement any recommendation.

### Overall Recommendation

Choose exactly one:

- Approve
- Approve with Changes
- Rework Required

## Final Restrictions

This is a read-only review.

Do not modify files.

Do not create commits.

Do not push changes.

Do not implement fixes.
