# Sprint 2 - Retrospective

**Author:** [Your Name]

## 1. Did the Sprint 1 improvements work?

| Improvement | Worked? | Evidence | Lesson |
|-------------|---------|----------|--------|
| Test-first (TDD) | Yes | Red CI runs on `test(...)` commits, green after `feat(...)` | Writing the test forced me to define behaviour (e.g. JSON 404 vs 500) before coding |
| flake8 in CI | Yes | `s2-ci-lint-coverage.png` | [e.g. First run flagged N issues I would not have seen otherwise] |
| Coverage gate (80%) | Yes | Coverage table in CI log | The gate is a safety net, not a goal: coverage does not prove the tests are good |
| Observability | Yes | Console logs, `/health` | Logs made it much faster to see what a request actually did |
| Evidence as I go | [Yes / Partly] | `docs/evidence/` | [Be honest here] |

## 2. What went well
* Test-first made the implementation commits small and predictable.
* Velocity stayed stable (7 then 6 points) with good estimate accuracy.
* The PR template with the DoD checklist kept every merge consistent.
* The retro actions were concrete, so it was easy to check whether they were applied.

## 3. What did not go well
* Intentional red CI runs made the pipeline look "broken" in the Actions list; I need a clearer convention (the PR title says `[red: test-first]`).
* The in-memory store means monitoring shows little real-world load; `/health` is only a liveness check.
* [Add a real difficulty you faced, e.g. a flake8 rule, Git branch mix-up, Windows curl quoting.]

## 4. Lessons learned
1. **Process improvements compound.** Small CI changes (lint, coverage) caught problems earlier than manual review.
2. **Test-first changes design, not just quality.** It pushed me to decide error behaviour up front.
3. **Visible, measurable retro actions get done;** vague ones ("plan better") do not.

## 5. Improvements for a Sprint 3
| # | Improvement | Measure of success |
|---|-------------|--------------------|
| 1 | Add a Dockerfile and a CD step (build and publish an image on merge to `main`) | Image published on every merge |
| 2 | Replace in-memory storage with SQLite and extend `/health` to check the database | Data survives restarts; `/health` reports DB status |
| 3 | Protect `main` (require PR + green CI) and add `pip-audit` for dependency scanning | Direct pushes to `main` blocked |
| 4 | Add integration tests against a running server | Separate integration job in CI |

## 6. Final reflection
Across two sprints, the biggest gain came not from the code (which is small) but from the
feedback loops: acceptance criteria that map to tests, a pipeline that gives feedback on every
push, and retrospectives that turned problems into specific changes that I could verify in the
next sprint.
