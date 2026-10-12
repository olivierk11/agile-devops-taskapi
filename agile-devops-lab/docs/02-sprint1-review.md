# Sprint 1 - Review

**Sprint dates:** [start] - [end]  **Author:** [Your Name]

## 1. Sprint Goal
> "A user can create, list and complete tasks through a REST API, with automated tests running in CI on every push."

**Goal met:** Yes / Partially  *(edit to match reality)*

## 2. Planned vs. Delivered

| Story | Points | Status | Evidence |
|-------|--------|--------|----------|
| US1 - Create a task | 3 | Done | PR #[n], tests `test_create_task_*` |
| US2 - List all tasks | 2 | Done | PR #[n], tests `test_list_tasks_*` |
| US3 - Complete a task | 2 | Done | PR #[n], tests `test_complete_task_*` |

**Velocity:** planned 7 pts / completed **7 pts**.

## 3. Acceptance Criteria Check

| AC | Result | How verified |
|----|--------|--------------|
| AC1.1 Valid title returns 201, status open | Pass | `test_create_task_returns_201_and_open_status` + demo |
| AC1.2 Title is trimmed | Pass | `test_create_task_trims_whitespace` |
| AC1.3 Invalid title returns 400 | Pass | 4 tests (empty, missing, no body, non-string) |
| AC1.4 IDs unique and increasing | Pass | `test_create_task_ids_increment` |
| AC2.1 Empty list returns `[]` | Pass | `test_list_tasks_empty` |
| AC2.2 All tasks returned in order | Pass | `test_list_tasks_returns_all_created` |
| AC3.1 Complete returns 200 / done | Pass | `test_complete_task_sets_status_done` |
| AC3.2 Status persisted | Pass | `test_complete_task_persists_in_list` |
| AC3.3 Unknown id returns 404 | Pass | `test_complete_unknown_task_returns_404` |

## 4. Demo

Start the app: `python -m src.app`, then:

```bash
# US1 - create
curl -i -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Study DevOps"}'
#  -> 201  {"id":1,"status":"open","title":"Study DevOps"}

# US1 - validation
curl -i -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": ""}'
#  -> 400  {"error":"title is required"}

# US2 - list
curl -i http://127.0.0.1:5000/tasks
#  -> 200  [{"id":1,"status":"open","title":"Study DevOps"}]

# US3 - complete
curl -i -X PATCH http://127.0.0.1:5000/tasks/1/complete
#  -> 200  {"id":1,"status":"done","title":"Study DevOps"}
```

**Screenshots** (in `docs/evidence/`):
* `s1-demo-create-list-complete.png` - terminal showing the calls above
* `s1-pytest-output.png` - local `pytest -v` (12 passed)
* `s1-ci-green.png` - GitHub Actions successful run
* `s1-board.png` - project board at the end of the sprint
* `s1-commit-history.png` - `git log --oneline --graph`

## 5. Testing Summary

| Metric | Value |
|--------|-------|
| Tests | **12** (7 for US1, 2 for US2, 3 for US3) |
| Result | 12 passed, 0 failed |
| CI | GitHub Actions: install + `pytest -v` |
| CI runs this sprint | [n] runs: [n] green, [n] red |

## 6. What Was Not Done / Issues
* Nothing from the sprint commitment was left undone.
* Data is stored in memory, so it is lost on restart (accepted limitation).
* [Add any real problem you hit, e.g. a failing CI run and how you fixed it.]

## 7. Product Owner Feedback (simulated)
* The core flow works end to end.
* Next priority: the operator needs visibility (health/logging), then delete and filter.

## 8. Updated Backlog
US4, US5, US7 are planned for Sprint 2. US6 stays in the backlog.
