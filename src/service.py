class TaskService:
    """Service class for managing tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if task is not None:
            task.mark_completed()
            return True
        return False
