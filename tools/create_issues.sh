#!/usr/bin/env bash
# OPTIONAL: creates one GitHub Issue per user story (needs the GitHub CLI: https://cli.github.com)
# Usage (from inside your cloned repo):  bash ../tools/create_issues.sh
set -e
gh auth status >/dev/null
for l in must should could; do gh label create "$l" --force >/dev/null 2>&1 || true; done
for l in sprint-1 sprint-2 backlog; do gh label create "$l" --force >/dev/null 2>&1 || true; done

mk() { gh issue create --title "$1" --label "$2" --label "$3" --body "$4"; }

mk "US1: Create a task (3 pts)" must sprint-1 "As a user, I want to create a task so that I can record what I need to do.

**AC:** valid title -> 201 + status open; blank/missing/non-string title -> 400; titles trimmed; ids increase."
mk "US2: List all tasks (2 pts)" must sprint-1 "As a user, I want to list all tasks so that I can see my workload.

**AC:** empty -> 200 []; otherwise all tasks in creation order."
mk "US3: Mark a task complete (2 pts)" must sprint-1 "As a user, I want to mark a task complete so that I can track my progress.

**AC:** existing id -> 200 status done (persisted); unknown id -> 404."
mk "US7: Health endpoint, logging, error handling (1 pt)" must sprint-2 "As an operator, I want a health endpoint, request logging and error handling so that I can monitor the service.

**AC:** /health -> 200 status/tasks/uptime; requests logged; JSON 404; logged JSON 500."
mk "US4: Delete a task (2 pts)" should sprint-2 "As a user, I want to delete a task so that I can remove mistakes.

**AC:** existing id -> 204 and removed; unknown id -> 404."
mk "US5: Filter tasks by status (3 pts)" should sprint-2 "As a user, I want to filter tasks by status so that I can focus on what is open.

**AC:** ?status=open|done filters; invalid -> 400; no param -> all."
mk "US6: Stronger input validation (3 pts)" could backlog "As a user, I want stronger input validation so that I do not corrupt my data.

**AC:** title > 100 chars -> 400; duplicate open title -> 409."
echo "Created 7 issues. Add them to your Project board."
