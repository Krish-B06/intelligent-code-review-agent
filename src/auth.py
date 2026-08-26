def can_modify_task(user, task_owner):
    return user == task_owner
