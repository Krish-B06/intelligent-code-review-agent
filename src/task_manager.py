from src.auth import can_modify_task


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def create_task(self, title, owner):
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = {
            "id": self.next_id,
            "title": title,
            "owner": owner,
            "completed": False,
        }

        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def complete_task(self, task_id, user):
        task = self.tasks[task_id]

        if not can_modify_task(user, task["owner"]):
            raise PermissionError("User cannot modify this task")

        task["completed"] = True
        return task

    def delete_task(self, task_id, user):
        task = self.tasks[task_id]

        if not can_modify_task(user, task["owner"]):
            raise PermissionError("User cannot modify this task")

        del self.tasks[task_id]

    def delete_task(self, task_id, user):
        del self.tasks[task_id]

    def update_task_title(self, task_id, user, title):
        self.tasks[task_id]["title"] = title
