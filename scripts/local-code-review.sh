#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

AGENT=".github/agents/code-review.agent.md"
INSTRUCTIONS=".github/instructions/code-review.instructions.md"
PROMPT=".github/prompts/code-review.prompt.md"

test -f "$AGENT"
test -f "$INSTRUCTIONS"
test -f "$PROMPT"

BASE_REF="${1:-main}"

echo "Preparing local code review..."
echo "Base: $BASE_REF"

rm -rf review-output
mkdir -p review-output

: > /tmp/review-changed-files.txt
: > /tmp/review.diff

# ------------------------------------------------------------
# 1. Committed changes between base and current branch
# ------------------------------------------------------------

git diff --name-only "$BASE_REF"...HEAD \
  >> /tmp/review-changed-files.txt

git diff "$BASE_REF"...HEAD \
  >> /tmp/review.diff

# ------------------------------------------------------------
# 2. Current uncommitted changes
# ------------------------------------------------------------

git diff --name-only \
  >> /tmp/review-changed-files.txt

git diff \
  >> /tmp/review.diff

# Include staged changes as well.
git diff --cached --name-only \
  >> /tmp/review-changed-files.txt

git diff --cached \
  >> /tmp/review.diff

# ------------------------------------------------------------
# Remove duplicates
# ------------------------------------------------------------

sort -u /tmp/review-changed-files.txt \
  -o /tmp/review-changed-files.txt

if [ ! -s /tmp/review.diff ]; then
    echo "No changes found to review."
    exit 0
fi

echo
echo "Files being reviewed:"
cat /tmp/review-changed-files.txt

echo
echo "Diff size:"
wc -c /tmp/review.diff

# ------------------------------------------------------------
# Build review prompt
# ------------------------------------------------------------

cat > /tmp/review-prompt.txt <<EOF2
You are performing a LOCAL repository code review.

Use the repository custom review agent:

$AGENT

Follow:

$INSTRUCTIONS

Use:

$PROMPT

============================================================
REVIEW SCOPE
============================================================

Review ONLY the developer changes supplied in:

/tmp/review.diff

Changed files:

/tmp/review-changed-files.txt

The repository itself may be inspected for additional context
when necessary to understand the changed project files.

Relevant requirements, acceptance criteria, architecture/design
documents, tests, and static-analysis results may also be inspected
when they exist in the repository.

Do NOT treat generated review artifacts as project source code.

============================================================
REVIEW REQUIREMENTS
============================================================

Review for:

1. Functional correctness
2. Requirements and acceptance criteria
3. Architecture and design compliance
4. Coding standards and maintainability
5. Security
6. Performance and scalability
7. Reliability and error handling
8. Testability and coverage
9. Static-analysis findings

Report only evidence-based findings.

Do not report speculative issues.

============================================================
MANDATORY RESTRICTIONS
============================================================

This is a READ-ONLY review.

Do NOT:

- modify source code
- modify configuration
- create commits
- push changes
- implement fixes
- automatically correct findings
- rewrite developer code

Only report observations, findings, and recommendations.

============================================================
OUTPUT
============================================================

Return the complete review using the exact output format
required by the custom review agent.

Return the review as text.
EOF2

# ------------------------------------------------------------
# Execute repository custom review agent
# ------------------------------------------------------------

copilot \
  --agent=code-review \
  -p "$(cat /tmp/review-prompt.txt)" \
  --output-format text \
  --deny-tool write \
  > review-output/local-review.md

test -s review-output/local-review.md

echo
echo "========================================"
echo "LOCAL CODE REVIEW"
echo "========================================"
cat review-output/local-review.md
