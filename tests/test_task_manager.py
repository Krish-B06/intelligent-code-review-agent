import pytest

from src.task_manager import TaskManager


def test_create_task():
    manager = TaskManager()

    task = manager.create_task("Test task", "alice")

    assert task["id"] == 1
    assert task["title"] == "Test task"
    assert task["owner"] == "alice"
    assert task["completed"] is False


def test_create_task_rejects_empty_title():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.create_task("   ", "alice")


def test_owner_can_complete_task():
    manager = TaskManager()
    task = manager.create_task("Test task", "alice")

    manager.complete_task(task["id"], "alice")

    assert task["completed"] is True


def test_non_owner_cannot_complete_task():
    manager = TaskManager()
    task = manager.create_task("Test task", "alice")

    with pytest.raises(PermissionError):
        manager.complete_task(task["id"], "bob")


def test_owner_can_delete_task():
    manager = TaskManager()
    task = manager.create_task("Test task", "alice")

    manager.delete_task(task["id"], "alice")

    assert task["id"] not in manager.tasks


def test_non_owner_cannot_delete_task():
    manager = TaskManager()
    task = manager.create_task("Test task", "alice")

    with pytest.raises(PermissionError):
        manager.delete_task(task["id"], "bob")


def test_completed_task_cannot_be_deleted():
    manager = TaskManager()
    task = manager.create_task("Test task", "alice")

    manager.complete_task(task["id"], "alice")

    with pytest.raises(ValueError):
        manager.delete_task(task["id"], "alice")

    assert task["id"] in manager.tasks


def test_owner_can_update_title():
    manager = TaskManager()
    task = manager.create_task("Old title", "alice")

    manager.update_task_title(task["id"], "alice", "New title")

    assert task["title"] == "New title"


def test_non_owner_cannot_update_title():
    manager = TaskManager()
    task = manager.create_task("Old title", "alice")

    with pytest.raises(PermissionError):
        manager.update_task_title(task["id"], "bob", "New title")

    assert task["title"] == "Old title"


def test_update_title_rejects_empty_title():
    manager = TaskManager()
    task = manager.create_task("Old title", "alice")

    with pytest.raises(ValueError):
        manager.update_task_title(task["id"], "alice", "   ")