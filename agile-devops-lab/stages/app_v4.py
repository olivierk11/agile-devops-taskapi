"""Task Manager API - a tiny Flask service for tracking tasks."""
import logging
import time

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger("taskapi")

app = Flask(__name__)

START_TIME = time.time()
VALID_STATUSES = ("open", "done")

tasks = []
_state = {"next_id": 1}


def reset_state():
    """Clear all tasks and restart ID numbering (used by the tests)."""
    tasks.clear()
    _state["next_id"] = 1


def _find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


@app.post("/tasks")
def create_task():
    """US1 - create a task. Requires a non-empty string title."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = {}
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify(error="title is required"), 400
    task = {"id": _state["next_id"], "title": title.strip(), "status": "open"}
    tasks.append(task)
    _state["next_id"] += 1
    return jsonify(task), 201


@app.get("/tasks")
def list_tasks():
    """US2 - list all tasks."""
    return jsonify(tasks), 200


@app.patch("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    """US3 - mark a task as done."""
    task = _find_task(task_id)
    if task is None:
        return jsonify(error="task not found"), 404
    task["status"] = "done"
    return jsonify(task), 200


@app.get("/health")
def health():
    """US7 - health endpoint for monitoring."""
    return jsonify(
        status="ok",
        tasks=len(tasks),
        uptime_seconds=round(time.time() - START_TIME, 1),
    ), 200


@app.before_request
def _start_timer():
    request._start = time.time()


@app.after_request
def _log_request(resp):
    elapsed_ms = (time.time() - getattr(request, "_start", time.time())) * 1000
    log.info("%s %s -> %s (%.1f ms)", request.method, request.path,
             resp.status_code, elapsed_ms)
    return resp


@app.errorhandler(Exception)
def _handle_error(exc):
    if isinstance(exc, HTTPException):
        return jsonify(error=exc.name.lower()), exc.code
    log.exception("Unhandled error")
    return jsonify(error="internal server error"), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
