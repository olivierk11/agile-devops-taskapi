"""Task Manager API - a tiny Flask service for tracking tasks."""
from flask import Flask, jsonify, request

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
