# Task Manager API

![CI](https://github.com/<your-username>/agile-devops-taskapi/actions/workflows/ci.yml/badge.svg)

A small Flask REST service for capturing, tracking and completing tasks.
Built for the **Agile & DevOps in Practice** final assessment and delivered over
two simulated sprints (Sprint 0 planning + Sprint 1 + Sprint 2).

**Product vision:** For students and busy professionals, the Task Manager API is a
lightweight service that lets users capture, track and complete tasks so nothing
gets forgotten. Unlike heavy tools, it is simple, fast and easy to integrate.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.app                # serves on http://127.0.0.1:5000
```

## API

| Method | Path                      | Description                          | Success |
|--------|---------------------------|--------------------------------------|---------|
| POST   | `/tasks`                  | Create a task `{"title": "..."}`     | 201     |
| GET    | `/tasks`                  | List tasks; optional `?status=open\|done` | 200 |
| PATCH  | `/tasks/<id>/complete`    | Mark a task as done                  | 200     |
| DELETE | `/tasks/<id>`             | Delete a task                        | 204     |
| GET    | `/health`                 | Health check (status, task count, uptime) | 200 |

Errors are always JSON: `{"error": "<message>"}` (400, 404, 500).

Example:

```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" \
     -d '{"title": "Study DevOps"}'
curl http://127.0.0.1:5000/tasks?status=open
curl http://127.0.0.1:5000/health
```

## Tests, lint and coverage

```bash
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
flake8 src tests
```

## Monitoring and logging

* Every request is logged to the console: `GET /health -> 200 (0.8 ms)`.
* Unhandled exceptions are logged with a stack trace and return a JSON 500.
* `GET /health` returns `{"status": "ok", "tasks": N, "uptime_seconds": S}`.

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs on every push: install,
flake8 lint, then pytest with an 80% coverage gate.

## Agile documentation

| Document | Purpose |
|----------|---------|
| [docs/01-sprint0-planning.md](docs/01-sprint0-planning.md) | Vision, backlog, estimates, acceptance criteria, DoD, Sprint 1 plan |
| [docs/02-sprint1-review.md](docs/02-sprint1-review.md) | Sprint 1 review |
| [docs/03-sprint1-retro.md](docs/03-sprint1-retro.md) | Sprint 1 retrospective |
| [docs/04-sprint2-plan.md](docs/04-sprint2-plan.md) | Sprint 2 plan, retro actions applied |
| [docs/05-sprint2-review.md](docs/05-sprint2-review.md) | Sprint 2 review |
| [docs/06-sprint2-retro.md](docs/06-sprint2-retro.md) | Sprint 2 retrospective |
| [docs/evidence/](docs/evidence/) | Screenshots: CI runs, tests, demos, board |

## Project layout

```
src/app.py          Flask application
tests/test_app.py   pytest suite
.github/workflows/  CI pipeline
docs/               Agile artefacts and evidence
```
