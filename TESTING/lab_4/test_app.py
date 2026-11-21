import json
import sqlite3

import pytest

from app import create_app, export_tasks


@pytest.fixture
def resources(tmp_path):
    db_path = tmp_path / "tasks.db"
    export_path = tmp_path / "tasks.json"
    app = create_app(db_path, export_path)
    return app.test_client(), db_path, export_path


def test_create_task(resources):
    client, db_path, export_path = resources

    response = client.post("/tasks", json={"title": "Вивчити pytest"})

    assert response.status_code == 201
    assert response.get_json()["title"] == "Вивчити pytest"
    with sqlite3.connect(db_path) as connection:
        row = connection.execute("SELECT title FROM tasks").fetchone()
    assert row == ("Вивчити pytest",)
    assert json.loads(export_path.read_text(encoding="utf-8"))[0]["title"] == "Вивчити pytest"


def test_get_tasks(resources):
    client, _, _ = resources
    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.get_json()] == [
        "Перше завдання",
        "Друге завдання",
    ]


def test_create_task_requires_title(resources):
    client, _, export_path = resources

    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert not export_path.exists()


# ---------- нові тести ----------

def test_export_empty_list(resources):
    _, db_path, export_path = resources

    export_tasks(db_path, export_path)

    assert json.loads(export_path.read_text(encoding="utf-8")) == []


def test_export_overwrites_corrupted_json(resources):
    client, db_path, export_path = resources
    client.post("/tasks", json={"title": "Завдання"})
    export_path.write_text("{ це не json", encoding="utf-8")

    export_tasks(db_path, export_path)

    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert [task["title"] for task in data] == ["Завдання"]


def test_tasks_order_in_db(resources):
    client, db_path, _ = resources

    client.post("/tasks", json={"title": "Перше"})
    client.post("/tasks", json={"title": "Друге"})

    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT id, title FROM tasks ORDER BY id").fetchall()
    assert rows == [(1, "Перше"), (2, "Друге")]


def test_create_task_without_title_not_saved(resources):
    client, db_path, _ = resources

    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert "error" in response.get_json()
    with sqlite3.connect(db_path) as connection:
        count = connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    assert count == 0


def test_delete_task(resources):
    client, db_path, export_path = resources
    client.post("/tasks", json={"title": "Перше"})
    client.post("/tasks", json={"title": "Друге"})

    response = client.delete("/tasks/1")

    assert response.status_code == 200
    with sqlite3.connect(db_path) as connection:
        rows = connection.execute("SELECT id, title FROM tasks").fetchall()
    assert rows == [(2, "Друге")]
    data = json.loads(export_path.read_text(encoding="utf-8"))
    assert [task["title"] for task in data] == ["Друге"]


def test_delete_missing_task(resources):
    client, _, _ = resources

    response = client.delete("/tasks/999")

    assert response.status_code == 404