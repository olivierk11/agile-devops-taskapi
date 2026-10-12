# Sprint 2 - Plan

**Author:** [Your Name]  **Date:** [DD/MM/YYYY]

## 1. Retro Actions Applied (from Sprint 1)

| # | Sprint 1 improvement | How it is applied in Sprint 2 | Evidence to look for |
|---|----------------------|-------------------------------|----------------------|
| 1 | Test-first (TDD) | Every story starts with a `test(...)` commit that fails, followed by the `feat(...)` commit that makes it pass | Commit history order; red then green CI runs |
| 2 | flake8 linting in CI | New step `flake8 src tests`, config in `.flake8` | `ci.yml` and CI log |
| 3 | Coverage gate | `pytest --cov=src --cov-fail-under=80` | Coverage table in CI log |
| 4 | Observability | US7: request logging, `/health`, JSON error handling | Console log screenshot, `/health` output |
| 5 | Capture evidence as I go | Screenshot after each CI run and merge | `docs/evidence/` filled during the sprint |

## 2. Sprint Goal
> "The service is observable (health endpoint and logs), and users can delete tasks and filter them by status, with every change developed test-first and checked by lint, tests and a coverage gate in CI."

## 3. Sprint Backlog

| Story | Points | Approach |
|-------|--------|----------|
| US7 - Health, logging, error handling | 1 | Tests first, then implementation |
| US4 - Delete a task | 2 | Tests first, then implementation |
| US5 - Filter tasks by status | 3 | Tests first, then implementation |
| **Committed total** | **6** | |

**Capacity:** 7 points (Sprint 1 velocity). Committed 6 rather than 7 to leave room for the
extra CI setup work (lint + coverage) that comes from the retro actions.
US6 (stronger validation, 3 pts) stays in the backlog.

## 4. Task Breakdown

| # | Task | Branch |
|---|------|--------|
| 1 | Add flake8 + coverage gate to CI (retro actions 2, 3) | `ci/lint-and-coverage` |
| 2 | Write failing tests for US7, then implement `/health`, logging, error handler | `feature/US7-monitoring` |
| 3 | Write failing tests for US4, then implement delete | `feature/US4-delete-task` |
| 4 | Write failing tests for US5, then implement filter | `feature/US5-filter-tasks` |
| 5 | Update README (API reference, monitoring section, CI badge) | `docs/sprint2` |
| 6 | Sprint Review, Sprint Retrospective | `docs/sprint2` |

## 5. Updated Definition of Done (v1.1)

All items from v1.0 plus:
- [ ] **Test committed before the feature** (TDD, retro action 1)
- [ ] **`flake8 src tests` is clean** (retro action 2)
- [ ] **Coverage >= 80%** enforced by CI (retro action 3)
- [ ] **New behaviour is observable** (logged where relevant)

## 6. Risks
| Risk | Mitigation |
|------|------------|
| Lint step fails on existing code | Run `flake8` locally before pushing the CI change and fix findings first |
| Test-first produces intentionally red CI runs | Use feature branches/PRs; only merge when green |
| Global error handler could hide 404s as 500s | Handle `HTTPException` separately and test it |
