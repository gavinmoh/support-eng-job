class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status


class TaskManager:
    def __init__(self):
        # dictionary is better than list for quick access by ID
        self.tasks = {}

    def add_task(self, id, title, priority):
        if id in self.tasks:
            return None

        task = Task(id, title, priority)
        self.tasks[id] = task
        return task

    def update_status(self, id, new_status):
        if id not in self.tasks:
            return False

        task = self.tasks[id]
        task.status = new_status
        return True

    def get_high_priority_tasks(self):
        # use list comprehension because it is cooler 😎
        return [task for _id, task in self.tasks.items() if task.priority == "high" or task.priority == 1]
