#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

AGENT=".github/agents/code-review.agent.md"

test -f "$AGENT"

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

# ------------------------------------------------------------
# 3. Staged changes
# ------------------------------------------------------------

git diff --cached --name-only \
  >> /tmp/review-changed-files.txt

git diff --cached \
  >> /tmp/review.diff

# ------------------------------------------------------------
# 4. Remove duplicate file names
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

cat > /tmp/review-prompt.txt <<EOF
You are performing a LOCAL repository code review.

Follow the review instructions defined in:

$AGENT

============================================================
REVIEW SCOPE
============================================================

Review ONLY the developer changes supplied in:

/tmp/review.diff

Changed files:

/tmp/review-changed-files.txt

Use relevant repository files as context when necessary.

Consider available requirements, acceptance criteria,
architecture/design documents, tests, coding standards,
security guidance, and static-analysis results.

Do not treat generated review artifacts as project source code.

============================================================
REVIEW RESTRICTIONS
============================================================

This is a READ-ONLY review.

Do NOT:

- modify source code
- modify configuration to fix issues
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
defined by the custom review agent.

Return the review as text.
EOF

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