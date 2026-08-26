from src.task_manager import TaskManager


def test_create_task():
    manager = TaskManager()

    task = manager.create_task("Review PR", "alice")

    assert task["title"] == "Review PR"
    assert task["owner"] == "alice"


def test_owner_can_complete_task():
    manager = TaskManager()
    task = manager.create_task("Review PR", "alice")

    result = manager.complete_task(task["id"], "alice")

    assert result["completed"] is True


def test_other_user_cannot_complete_task():
    manager = TaskManager()
    task = manager.create_task("Review PR", "alice")

    try:
        manager.complete_task(task["id"], "bob")
        assert False
    except PermissionError:
        pass
