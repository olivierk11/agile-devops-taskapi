# Agile & DevOps Final Assessment: Complete Step-by-Step Guide

This package gives you everything to finish the lab: working Python code, all documents, CI workflows, and a **commit playbook** that builds a genuine, iterative Git history.

> **Read this first: make it yours.** The code is tested and ready, but the documents are *drafts*. Your retrospectives, dates, PR numbers and "problems I hit" must reflect what **you** actually did. Graders read reflections for honesty, and a retro that doesn't match your commit history is easy to spot. Replace every `[bracket]` placeholder.

---

## 1. What's in the package

```
agile-lab/
├── GUIDE.md                  <- this file
├── final-repo/               <- the finished project (REFERENCE: do not push this folder)
│   ├── src/app.py            final application
│   ├── tests/test_app.py     final tests (22)
│   ├── docs/01..06 *.md      all Agile documents
│   ├── docs/evidence/        screenshots go here
│   └── .github/              CI workflow + PR template
├── stages/                   <- step-by-step versions of each file (you copy these in order)
│   ├── app_v1..v6.py         application after US1, US2, US3, US7, US4, US5
│   ├── test_app_v1..v6.py    tests after each of those stories
│   ├── ci_v1.yml             Sprint 1 pipeline (install + pytest)
│   ├── requirements_v1.txt   Sprint 1 dependencies
│   └── README_v1.md          initial README
└── tools/create_issues.sh    optional: creates the 7 GitHub issues for you
```

**Why stages?** The rubric gives 20% for *iterative commits*. Stages let you commit each story in the same incremental order a real developer would, with Sprint 2 following **test-first** (failing test commit, then the feature commit).

**Important:** do the playbook over real working sessions (e.g. one sprint per day or two), not in ten minutes. Commit timestamps are visible.

---

## 2. Prerequisites (15 min)

1. **Git**: `git --version`. Install from git-scm.com (on Windows this also gives you **Git Bash**, which I recommend for every command below).
2. **Python 3.11+**: `python --version` (or `python3 --version`).
3. A **GitHub account**.
4. Tell Git who you are (once):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"   # use the email on your GitHub account
   ```
5. Optional: GitHub CLI (`gh`) for issues and PRs. The web UI works fine too.

---

## 3. Phase A: GitHub setup (20 min)

1. On GitHub: **New repository** named `agile-devops-taskapi`. Choose **Public** (or private and invite your instructor later). Do **not** add a README (we add our own).
2. Unzip this package into a folder, e.g. `~/agile-lab/`. Then clone **inside** it:
   ```bash
   cd ~/agile-lab
   git clone https://github.com/<your-username>/agile-devops-taskapi.git
   cd agile-devops-taskapi
   git branch -M main
   ```
3. **Project board** (Agile evidence): GitHub, Projects, New project, **Board**. Columns: `Backlog`, `Sprint Todo`, `In Progress`, `Done`. Add custom field **Story Points**.
4. **Issues**: create one Issue per user story (US1 to US7), either manually (copy from `docs/01-sprint0-planning.md`) or run `bash ../tools/create_issues.sh` once `gh auth login` is done. Add them to the board. Put US1-US3 in `Sprint Todo`, the rest in `Backlog`.
5. 📸 **Screenshot:** `s0-board-initial.png` (all stories on the board).

---

## 4. Phase B: Commit playbook

Commands run from inside `agile-devops-taskapi/`. `../stages` and `../final-repo` are the package folders. (Windows PowerShell users: `cp` works as an alias for `Copy-Item`, but Git Bash is simpler.)

Merge rule for all PRs: choose **"Create a merge commit"** (not squash) so each of your commits stays in the history.

### SPRINT 0: Planning (commits 1 to 4, directly on `main`)

```bash
# Commit 1
cp ../stages/README_v1.md README.md
cp ../final-repo/.gitignore .
git add README.md .gitignore
git commit -m "chore: initialize repository with README and .gitignore"

# Commit 2  (edit the [placeholders] in the file FIRST: name, date)
mkdir -p docs/evidence
cp ../final-repo/docs/01-sprint0-planning.md docs/
git add docs
git commit -m "docs(sprint0): add vision, backlog, acceptance criteria, DoD and Sprint 1 plan"

# Commit 3
mkdir -p .github
cp ../final-repo/.github/pull_request_template.md .github/
git add .github
git commit -m "chore: add pull request template with DoD checklist"

# Commit 4
cp ../stages/requirements_v1.txt requirements.txt
cp ../final-repo/pytest.ini .
mkdir -p src tests && touch src/__init__.py tests/__init__.py
git add requirements.txt pytest.ini src tests
git commit -m "chore: add python project skeleton and dependencies"

git push -u origin main
```

Set up your environment (not committed, `.venv` is git-ignored):
```bash
python -m venv .venv
source .venv/bin/activate          # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
```

### SPRINT 1: Execution (commits 5 to 13)

Move issues US1-US3 to **In Progress** on the board as you start each. Put each story in a PR with `Closes #<issue>` in the description.

**US1: create a task**
```bash
git switch -c feature/US1-create-task
cp ../stages/app_v1.py src/app.py
git add src/app.py
git commit -m "feat(US1): add POST /tasks endpoint"

cp ../stages/test_app_v1.py tests/test_app.py
pytest -v                                    # expect: 7 passed
git add tests/test_app.py
git commit -m "test(US1): add unit tests for task creation"

git push -u origin feature/US1-create-task
```
On GitHub: open a Pull Request into `main`, fill in the template, **merge (merge commit)**. Then:
```bash
git switch main && git pull
```

**CI pipeline**
```bash
git switch -c ci/add-pipeline
mkdir -p .github/workflows
cp ../stages/ci_v1.yml .github/workflows/ci.yml
git add .github/workflows/ci.yml
git commit -m "ci: add GitHub Actions workflow running pytest"
git push -u origin ci/add-pipeline
```
Open the **Actions** tab and watch it run. 📸 `s1-ci-green.png`.

*Optional but impressive: red, then green.* On this same branch:
```bash
# temporarily break one assertion in tests/test_app.py (e.g. change 201 to 200), then:
git commit -am "test: temporarily break assertion to verify CI catches failures"
git push                                     # CI turns RED -> screenshot s1-ci-red.png
git revert HEAD --no-edit                    # restore the test
git push                                     # CI turns GREEN
```
Open a PR and merge it. `git switch main && git pull`.

**US2: list tasks**
```bash
git switch -c feature/US2-list-tasks
cp ../stages/app_v2.py src/app.py
git add src/app.py && git commit -m "feat(US2): add GET /tasks endpoint"
cp ../stages/test_app_v2.py tests/test_app.py
pytest -v                                    # expect: 9 passed
git add tests/test_app.py && git commit -m "test(US2): add tests for listing tasks"
git push -u origin feature/US2-list-tasks    # open PR, wait for green check, merge
git switch main && git pull
```

**US3: complete a task**
```bash
git switch -c feature/US3-complete-task
cp ../stages/app_v3.py src/app.py
git add src/app.py && git commit -m "feat(US3): add PATCH /tasks/<id>/complete endpoint"
cp ../stages/test_app_v3.py tests/test_app.py
pytest -v                                    # expect: 12 passed
git add tests/test_app.py && git commit -m "test(US3): add tests for completing tasks"
git push -u origin feature/US3-complete-task # PR, green check, merge
git switch main && git pull
```

**Demo and evidence** (run the app in one terminal, `curl` in another; commands are in `docs/02-sprint1-review.md`):
```bash
python -m src.app
```
> Windows PowerShell: use `curl.exe` and escape quotes (`-d '{\"title\":\"A\"}'`), or just use Git Bash / Postman.

📸 `s1-demo-create-list-complete.png`, `s1-pytest-output.png`, `s1-commit-history.png` (`git log --oneline --graph`), `s1-board.png` (all three stories in Done).

**Sprint 1 documents**
```bash
git switch -c docs/sprint1
cp ../final-repo/docs/02-sprint1-review.md ../final-repo/docs/03-sprint1-retro.md docs/
# EDIT both files: fill the brackets, add your real numbers and the real problems you hit.
# Save your Sprint 1 screenshots into docs/evidence/ using the names listed in docs/evidence/README.md

git add docs/02-sprint1-review.md docs/evidence
git commit -m "docs(sprint1): add sprint review with demo evidence"
git add docs/03-sprint1-retro.md
git commit -m "docs(sprint1): add sprint retrospective with improvements for sprint 2"
git push -u origin docs/sprint1              # open PR and merge
git switch main && git pull
git tag -a v0.1.0 -m "Sprint 1: create, list, complete tasks" && git push origin v0.1.0
```

### SPRINT 2: Execution and Improvement (commits 14 to 25)

Commit the plan first, directly on `main`:
```bash
cp ../final-repo/docs/04-sprint2-plan.md docs/
git add docs/04-sprint2-plan.md
git commit -m "docs(sprint2): add sprint 2 plan with retro actions applied"
git push
```

**Retro actions 2 and 3: lint + coverage in CI**
```bash
git switch -c ci/lint-and-coverage
cp ../final-repo/requirements.txt .
cp ../final-repo/.flake8 .
cp ../final-repo/.github/workflows/ci.yml .github/workflows/ci.yml
pip install -r requirements.txt
flake8 src tests                                       # must print nothing
pytest -v --cov=src --cov-fail-under=80                # must pass
git add requirements.txt .flake8 .github/workflows/ci.yml
git commit -m "ci: add flake8 lint and 80% coverage gate (retro actions 2 and 3)"
git push -u origin ci/lint-and-coverage                # PR, green, merge
git switch main && git pull
```
📸 `s2-ci-lint-coverage.png` (open the run log and show the flake8 step and the coverage table).

**Test-first pattern for each story (retro action 1).** For each story below, the first commit is the **test** and CI goes **red**. Open the PR right after pushing that commit (title it like `[red: test-first] US7 ...`). Then push the feature commit and CI goes **green**.

**US7: health, logging, error handling**
```bash
git switch -c feature/US7-monitoring
cp ../stages/test_app_v4.py tests/test_app.py
pytest -v                                              # expect 5 FAILED (that's the point)
git add tests/test_app.py
git commit -m "test(US7): add failing tests for health endpoint, logging and error handling"
git push -u origin feature/US7-monitoring              # open PR -> CI RED -> screenshot s2-ci-red.png

cp ../stages/app_v4.py src/app.py
pytest -v                                              # expect 17 passed
git add src/app.py
git commit -m "feat(US7): add /health endpoint, request logging and JSON error handler"
git push                                               # CI GREEN -> screenshot s2-ci-green.png; merge
git switch main && git pull
```

**US4: delete a task**
```bash
git switch -c feature/US4-delete-task
cp ../stages/test_app_v5.py tests/test_app.py          # 2 new tests fail
git add tests/test_app.py && git commit -m "test(US4): add failing tests for deleting a task"
git push -u origin feature/US4-delete-task             # open PR (red)
cp ../stages/app_v5.py src/app.py                      # pytest -> 19 passed
git add src/app.py && git commit -m "feat(US4): add DELETE /tasks/<id> endpoint"
git push                                               # green, merge
git switch main && git pull
```

**US5: filter by status**
```bash
git switch -c feature/US5-filter-tasks
cp ../stages/test_app_v6.py tests/test_app.py          # 3 new tests fail
git add tests/test_app.py && git commit -m "test(US5): add failing tests for status filter"
git push -u origin feature/US5-filter-tasks            # open PR (red)
cp ../stages/app_v6.py src/app.py                      # pytest -> 22 passed
git add src/app.py && git commit -m "feat(US5): add ?status= filter to GET /tasks"
git push                                               # green, merge
git switch main && git pull
```

**Demo and monitoring evidence:** run `python -m src.app` and run the Sprint 2 `curl` commands from `docs/05-sprint2-review.md`.
📸 `s2-console-logs.png` (the terminal running the app showing request log lines), `s2-health-endpoint.png`, `s2-demo-delete-filter.png`, `s2-pytest-output.png` (22 passed).

**Final docs**
```bash
git switch -c docs/sprint2
cp ../final-repo/README.md .                           # replace <your-username> in the CI badge URL!
git add README.md && git commit -m "docs: update README with API reference, monitoring and CI badge"

cp ../final-repo/docs/05-sprint2-review.md docs/       # edit, add screenshots
git add docs/05-sprint2-review.md docs/evidence
git commit -m "docs(sprint2): add sprint 2 review with sprint comparison"

cp ../final-repo/docs/06-sprint2-retro.md docs/        # edit honestly
cp ../final-repo/docs/evidence/README.md docs/evidence/
git add docs/06-sprint2-retro.md docs/evidence/README.md
git commit -m "docs(sprint2): add sprint 2 retrospective and lessons learned"
git push -u origin docs/sprint2                        # PR and merge
git switch main && git pull
git tag -a v0.2.0 -m "Sprint 2: monitoring, delete, filter" && git push origin v0.2.0
```

Finally, mark all issues Done on the board. 📸 `s2-board.png`, `s2-commit-history.png`.

---

## 5. Final verification (10 min)

Run these from `main`, right after `git pull`:

```bash
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80   # 22 passed
flake8 src tests                                                    # no output
git log --oneline | wc -l                                           # aim for 20+ commits
git log --oneline --graph --all                                     # branches visible
```

Compare your repo against `final-repo/` (code and docs should match; only your edits to docs differ):
```bash
diff -r src ../final-repo/src && diff -r tests ../final-repo/tests && echo "code matches"
```

Then check the GitHub **Actions** tab is green on `main`, and that no `[placeholder]` brackets remain:
```bash
grep -rn "\[Your Name\]\|\[n\]\|\[DD/MM\|<your-username>" docs README.md
```

---

## 6. Submission checklist (maps to the rubric)

| Deliverable | Where | Done |
|---|---|---|
| 1. Backlog and sprint plans | `docs/01-sprint0-planning.md`, `docs/04-sprint2-plan.md` | ☐ |
| 2. Codebase + incremental history | GitHub repo URL (20+ commits, PRs, tags) | ☐ |
| 3. CI/CD evidence | `.github/workflows/ci.yml`, `s1-ci-green.png`, `s2-ci-red.png`, `s2-ci-green.png`, `s2-ci-lint-coverage.png` | ☐ |
| 4. Testing evidence | `s1-pytest-output.png` (12), `s2-pytest-output.png` (22), coverage table | ☐ |
| 5. Sprint reviews | `docs/02-...`, `docs/05-...` with screenshots | ☐ |
| 6. Retrospectives | `docs/03-...`, `docs/06-...` | ☐ |

**What to hand in:** the GitHub repository link (and make sure the grader can open it) plus, if required, a zip of the repo (`git archive -o submission.zip HEAD`).

| Rubric dimension | Weight | Where you earn it |
|---|---|---|
| Agile practice | 25% | Prioritised backlog, estimates, Given/When/Then ACs, DoD, sprint goals and plans, board |
| DevOps practice | 25% | Working CI, lint + coverage gate, tests in pipeline, `/health` + logging |
| Delivery discipline | 20% | Branch per story, test/feat commits, PRs, tags, no big-bang commit |
| Prototype quality | 20% | 22 passing tests, all ACs verified in the reviews |
| Reflection | 10% | Retro 1 problems become Sprint 2 actions, retro 2 checks them with evidence |

---

## 7. Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'src'` | Run `pytest` from the repo root (where `pytest.ini` lives), with the venv active. |
| `flake8` complains in CI | Read the message (file:line:code) and fix it. Always run `flake8 src tests` locally before pushing. |
| Coverage gate fails | Run `pytest --cov=src --cov-report=term-missing` and see which lines are untested. |
| Actions tab shows nothing | Repo, Settings, Actions, General: enable Actions. Make sure the file is at `.github/workflows/ci.yml`. |
| `git push` rejected | `git pull --rebase`, then push again. |
| Authentication fails on push | GitHub no longer accepts passwords. Use a Personal Access Token, or `gh auth login`. |
| Port 5000 already in use (macOS AirPlay) | Change the port in `src/app.py`'s last line, or turn off AirPlay Receiver. |
| `touch` not found (PowerShell) | Use Git Bash, or `New-Item src/__init__.py`. |
| Accidentally committed `.venv` | `git rm -r --cached .venv`, commit; `.gitignore` already lists it. |

---

## 8. Suggested schedule

| Block | Time | Work |
|---|---|---|
| Sprint 0 | 1-2 h | Phase A, commits 1-4, board and issues |
| Sprint 1 | 3-4 h | US1-US3, CI, demo, review, retro |
| Sprint 2 | 3 h | CI lint/coverage, US7/US4/US5 test-first, demo, review, retro |
| Polish | 1 h | Section 5 verification, fill placeholders, submit |

Good luck. Keep your commits small and your reflections honest, and the rubric takes care of itself.
