# Sprint 2 - Review

**Sprint dates:** [start] - [end]  **Author:** [Your Name]

## 1. Sprint Goal
> "The service is observable (health endpoint and logs), and users can delete tasks and filter them by status, with every change developed test-first and checked by lint, tests and a coverage gate in CI."

**Goal met:** Yes / Partially  *(edit to match reality)*

## 2. Planned vs. Delivered

| Story | Points | Status | Evidence |
|-------|--------|--------|----------|
| US7 - Health, logging, error handling | 1 | Done | PR #[n] |
| US4 - Delete a task | 2 | Done | PR #[n] |
| US5 - Filter tasks by status | 3 | Done | PR #[n] |

**Velocity:** planned 6 pts / completed **6 pts**.

## 3. Acceptance Criteria Check

| AC | Result | How verified |
|----|--------|--------------|
| AC7.1 `/health` returns status, count, uptime | Pass | `test_health_returns_ok`, `test_health_reports_task_count` |
| AC7.2 Requests logged with method/path/status/time | Pass | `test_requests_are_logged` + console screenshot |
| AC7.3 Unknown route returns JSON 404 | Pass | `test_unknown_route_returns_json_404` |
| AC7.4 Unhandled error logged, JSON 500 | Pass | `test_unhandled_exception_returns_json_500` |
| AC4.1 Delete returns 204 and removes task | Pass | `test_delete_task_returns_204_and_removes_it` |
| AC4.2 Delete unknown id returns 404 | Pass | `test_delete_unknown_task_returns_404` |
| AC5.1 / 5.2 Filter open / done | Pass | `test_filter_open_tasks`, `test_filter_done_tasks` |
| AC5.3 Invalid status returns 400 | Pass | `test_filter_invalid_status_returns_400` |
| AC5.4 No filter returns all | Pass | existing US2 tests still pass |

## 4. Demo

```bash
curl -i http://127.0.0.1:5000/health
#  -> 200  {"status":"ok","tasks":0,"uptime_seconds":12.3}

curl -s -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "A"}'
curl -s -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "B"}'
curl -s -X PATCH http://127.0.0.1:5000/tasks/2/complete

curl -s "http://127.0.0.1:5000/tasks?status=open"     # -> only task A
curl -s "http://127.0.0.1:5000/tasks?status=done"     # -> only task B
curl -i "http://127.0.0.1:5000/tasks?status=banana"   # -> 400
curl -i -X DELETE http://127.0.0.1:5000/tasks/1       # -> 204
curl -i http://127.0.0.1:5000/nope                    # -> 404 JSON
```

Console output while running the demo (monitoring evidence):

```
2026-.. INFO taskapi GET /health -> 200 (0.9 ms)
2026-.. INFO taskapi POST /tasks -> 201 (0.4 ms)
2026-.. INFO taskapi PATCH /tasks/2/complete -> 200 (0.3 ms)
2026-.. INFO taskapi GET /tasks -> 200 (0.2 ms)
2026-.. INFO taskapi GET /tasks -> 400 (0.2 ms)
2026-.. INFO taskapi DELETE /tasks/1 -> 204 (0.2 ms)
2026-.. INFO taskapi GET /nope -> 404 (0.2 ms)
```
*(Replace with a real paste/screenshot from your own run.)*

**Screenshots** (in `docs/evidence/`):
* `s2-console-logs.png`, `s2-health-endpoint.png`, `s2-demo-delete-filter.png`
* `s2-ci-red.png` (failing test-first run) and `s2-ci-green.png` (after implementation)
* `s2-ci-lint-coverage.png` (lint step and coverage table in the log)
* `s2-pytest-output.png` (22 passed), `s2-board.png`, `s2-commit-history.png`

## 5. Sprint 1 vs. Sprint 2 Comparison

| Metric | Sprint 1 | Sprint 2 |
|--------|----------|----------|
| Points planned / completed | 7 / 7 | 6 / 6 |
| Stories delivered | 3 | 3 |
| Tests at end of sprint | 12 | **22** (+10) |
| API routes | 3 | 5 |
| CI steps | install, test | install, **lint, test + coverage gate** |
| Test written before code | No | **Yes** (all 3 stories) |
| Monitoring | None | Request logs, `/health`, JSON errors |
| Coverage | not measured | [fill from CI log, e.g. 9x%] |
| CI duration | [e.g. 25s] | [e.g. 35s] |
| Failed CI runs | [n] | [n] (intentional red test-first runs: [n]) |
| Commits | [n] | [n] |

## 6. Retro Actions - Result
| Action | Result |
|--------|--------|
| Test-first | Done. Each `test(...)` commit precedes its `feat(...)` commit; CI went red then green. |
| flake8 in CI | Done. Pipeline enforces lint. |
| Coverage gate | Done. Gate at 80%, actual [x]%. |
| Observability | Done (US7). |
| Evidence as I go | [Done / Partly: explain] |

## 7. Not Done / Known Limitations
* US6 (stronger validation) remains in the backlog by design.
* Storage is in memory: data is lost on restart.
* `/health` reports liveness only, not dependency checks (there are no dependencies yet).

## 8. Updated Backlog / Next Sprint Candidates
US6 validation, persistent storage (SQLite), Dockerfile + CD deployment, due dates for tasks.
