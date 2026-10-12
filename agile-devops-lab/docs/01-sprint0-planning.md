# Sprint 0 - Planning

**Project:** Task Manager API  **Author:** [Your Name]  **Date:** [DD/MM/YYYY]
**Stack:** Python 3.11, Flask, pytest, flake8, GitHub Actions

---

## 1. Product Vision

> For students and busy professionals, the **Task Manager API** is a lightweight
> service that lets users capture, track and complete tasks so nothing gets
> forgotten. Unlike heavy project-management tools, it is simple, fast and easy
> to integrate into any other application.

**Product Owner (simulated):** [Your Name]  **Developer / Scrum Master:** [Your Name]

---

## 2. Product Backlog (prioritised)

Estimation uses **relative sizing with Fibonacci story points** (1, 2, 3, 5, 8).
Reference story: **US2 (list tasks) = 2 points**, because it is a single read-only
endpoint with no business rules. All other stories were sized relative to it.

Priority uses **MoSCoW**, ordered by business value first, then by dependency
(you cannot complete or delete a task that cannot be created).

| Rank | ID  | User Story | Priority | Points | Planned Sprint |
|------|-----|------------|----------|--------|----------------|
| 1 | US1 | As a user, I want to **create a task** so that I can record what I need to do | Must | 3 | Sprint 1 |
| 2 | US2 | As a user, I want to **list all tasks** so that I can see my workload | Must | 2 | Sprint 1 |
| 3 | US3 | As a user, I want to **mark a task complete** so that I can track my progress | Must | 2 | Sprint 1 |
| 4 | US7 | As an operator, I want a **health endpoint, request logging and error handling** so that I can monitor the service | Must | 1 | Sprint 2 |
| 5 | US4 | As a user, I want to **delete a task** so that I can remove mistakes | Should | 2 | Sprint 2 |
| 6 | US5 | As a user, I want to **filter tasks by status** so that I can focus on what is open | Should | 3 | Sprint 2 |
| 7 | US6 | As a user, I want **stronger input validation** (title length, duplicates) so that I do not corrupt my data | Could | 3 | Sprint 3 (backlog) |

**Total backlog:** 16 points.  Basic title validation is already part of US1; US6 covers the extras.

### Prioritisation rationale
* US1-US3 form the **minimum viable product**: without them there is nothing to demo.
* US7 is a *Must* for the product but is deliberately scheduled in Sprint 2 because
  the assessment requires monitoring to be added after the CI/testing foundation.
* US4 and US5 are valuable but the product is usable without them.
* US6 is a *Could*: nice to have, lowest risk if dropped.

---

## 3. Acceptance Criteria (Given / When / Then)

### US1 - Create a task
* **AC1.1** Given a valid title, when I `POST /tasks`, then I receive `201` and a task with an `id`, the `title` and `status = "open"`.
* **AC1.2** Given a title with surrounding spaces, when I create the task, then the stored title is trimmed.
* **AC1.3** Given an empty, blank, missing or non-string title (or no body), when I `POST /tasks`, then I receive `400` and `{"error": "..."}`.
* **AC1.4** Given two successful creations, then the IDs are unique and increasing.

### US2 - List all tasks
* **AC2.1** Given no tasks exist, when I `GET /tasks`, then I receive `200` and `[]`.
* **AC2.2** Given tasks exist, when I `GET /tasks`, then I receive `200` and all tasks in creation order.

### US3 - Complete a task
* **AC3.1** Given an existing task, when I `PATCH /tasks/<id>/complete`, then I receive `200` and `status = "done"`.
* **AC3.2** Given a completed task, when I list tasks, then the new status is persisted.
* **AC3.3** Given an unknown id, when I call the endpoint, then I receive `404` with an error message.

### US7 - Health, logging and error handling
* **AC7.1** When I `GET /health`, then I receive `200` and `{"status": "ok", "tasks": N, "uptime_seconds": S}`.
* **AC7.2** Every handled request is logged to the console with method, path, status code and duration.
* **AC7.3** Given an unknown route, then I receive a JSON `404` (not an HTML page).
* **AC7.4** Given an unexpected exception, then the error is logged with a stack trace and I receive a JSON `500` that does not leak internals.

### US4 - Delete a task
* **AC4.1** Given an existing task, when I `DELETE /tasks/<id>`, then I receive `204` and the task no longer appears in the list.
* **AC4.2** Given an unknown id, then I receive `404` with an error message.

### US5 - Filter by status
* **AC5.1** When I `GET /tasks?status=open`, then only open tasks are returned.
* **AC5.2** When I `GET /tasks?status=done`, then only completed tasks are returned.
* **AC5.3** Given an invalid status value, then I receive `400` with an error message.
* **AC5.4** Given no `status` parameter, then all tasks are returned (US2 behaviour unchanged).

### US6 - Stronger validation (backlog, not yet refined)
* **AC6.1** Given a title longer than 100 characters, then I receive `400`.
* **AC6.2** Given a duplicate open title, then I receive `409`.

---

## 4. Definition of Done (applies to every story)

A story is **Done** only when ALL of these are true:

- [ ] Code is committed on a feature branch with small, meaningful commits and merged through a Pull Request
- [ ] Unit/integration tests cover every acceptance criterion and pass locally
- [ ] The CI pipeline is green on the branch/PR
- [ ] All acceptance criteria are manually verified (curl/Postman) and recorded in the Sprint Review
- [ ] README / docs are updated when behaviour changes
- [ ] No known critical bugs remain

*(The DoD is tightened in Sprint 2: lint clean, coverage >= 80% and tests written first. See `04-sprint2-plan.md`.)*

---

## 5. Sprint 1 Plan

**Sprint length:** 1 simulated sprint  **Capacity (assumed):** 8 story points (single developer, first sprint so a cautious estimate)

**Sprint goal:** *"A user can create, list and complete tasks through a REST API, with automated tests running in CI on every push."*

| Story | Points |
|-------|--------|
| US1 - Create a task | 3 |
| US2 - List all tasks | 2 |
| US3 - Complete a task | 2 |
| **Committed total** | **7** (within the 8-point capacity) |

### Task breakdown

| # | Task | Story | Branch |
|---|------|-------|--------|
| 1 | Project skeleton, dependencies, `.gitignore`, PR template | - | `main` |
| 2 | Implement `POST /tasks` | US1 | `feature/US1-create-task` |
| 3 | Unit tests for US1 | US1 | `feature/US1-create-task` |
| 4 | GitHub Actions workflow (install + pytest) | - | `ci/add-pipeline` |
| 5 | Implement `GET /tasks` + tests | US2 | `feature/US2-list-tasks` |
| 6 | Implement `PATCH /tasks/<id>/complete` + tests | US3 | `feature/US3-complete-task` |
| 7 | Verify acceptance criteria, write Sprint Review | - | `docs/sprint1` |
| 8 | Retrospective | - | `docs/sprint1` |

### Risks
| Risk | Mitigation |
|------|------------|
| First time configuring GitHub Actions | Keep the workflow minimal; add steps incrementally |
| In-memory storage loses data on restart | Accepted for the prototype; noted as a future backlog item |
| Scope creep | Anything outside US1-US3 goes to the backlog |

### Workflow agreements
* One feature branch per story, merged with a Pull Request (merge commit, not squash, to preserve history).
* Conventional commit messages: `feat`, `test`, `ci`, `docs`, `chore`, `fix`.
* Commit at least once per task.
