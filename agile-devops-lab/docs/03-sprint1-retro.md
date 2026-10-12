# Sprint 1 - Retrospective

**Format:** Went well / Didn't go well / Start-Stop-Continue  **Author:** [Your Name]

## 1. Data
| Metric | Value |
|--------|-------|
| Committed / completed | 7 / 7 points |
| Tests at end of sprint | 12 |
| Commits | [n] |
| Failed CI runs | [n] |

## 2. What went well
* Small, focused branches (one per story) made PRs easy to review and revert.
* Clear Given/When/Then acceptance criteria translated almost directly into test names.
* CI was green by the end and caught problems before merging.
* Estimates were accurate (7 planned, 7 delivered).

## 3. What did not go well
1. **Tests were written after the code** (`feat` commit, then `test` commit), so tests only confirmed what I had already built, and edge cases such as non-string titles were found late.
2. **CI only ran `pytest`.** Style problems and unused code were not checked, and nothing stopped test coverage from silently dropping.
3. **The running service was a black box.** When debugging a request I had no logs and no way to check that the app was alive.
4. **Evidence was captured at the end**, so I had to re-create some screenshots and some CI history was cleaned up by then.

## 4. Start / Stop / Continue
| Start | Stop | Continue |
|-------|------|----------|
| Writing the test first (TDD) | Writing tests after the feature | One branch per story |
| Linting in CI (flake8) | Merging without a quality gate | Conventional commit messages |
| A coverage gate in CI | Leaving screenshots to the end | Given/When/Then acceptance criteria |
| Logging + health endpoint | | Merging through PRs with the DoD checklist |

## 5. Improvements for Sprint 2 (specific and measurable)

| # | Improvement | How it will be applied | Success measure |
|---|-------------|------------------------|-----------------|
| 1 | **Test-first (TDD)** for every story | Commit the failing `test(...)` commit first, then the `feat(...)` commit | History shows a `test` commit before each `feat` commit; CI shows a red then green run |
| 2 | **Add flake8 linting to CI** | New CI step `flake8 src tests`, `.flake8` config | Pipeline fails on style errors; lint is clean at sprint end |
| 3 | **Add a coverage gate** | `pytest --cov=src --cov-fail-under=80` in CI | Coverage >= 80% reported in the CI log |
| 4 | **Add observability** | Request logging, `/health`, JSON error handler (US7) | Logs visible in the console; `/health` returns 200 |
| 5 | **Capture evidence as I go** | Screenshot after every green/red CI run and merged PR | Evidence folder complete before the review is written |

## 6. Action for the Definition of Done
DoD is updated for Sprint 2 to add: "flake8 clean", "coverage >= 80%", "test committed before the feature".
