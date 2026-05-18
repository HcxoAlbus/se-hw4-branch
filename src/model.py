class Task:
    """A simple task model."""

    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Unfinished"
        return f"Task(id={self.task_id}, title='{self.title}', status='{status}')"
