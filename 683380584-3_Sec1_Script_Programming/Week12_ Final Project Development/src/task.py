import datetime

class Task:
    def __init__(self, id, description, completed=False, tags=None):
        self.id = id
        self.description = description
        self.completed = completed
        self.tags = tags if tags is not None else []

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "tags": self.tags,
            "_type": "Task"
        }

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        tags_str = f" | Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"ID: {self.id} | Description: {self.description} | Status: {status}{tags_str}"


class DueDateTask(Task):
    def __init__(self, id, description, due_date, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        if isinstance(due_date, str):
            self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        else:
            self.due_date = due_date

    def to_dict(self):
        data = super().to_dict()
        data["due_date"] = self.due_date.strftime('%Y-%m-%d')
        data["_type"] = "DueDateTask"
        return data

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Due: {self.due_date.strftime('%Y-%m-%d')}"


class PriorityTask(Task):
    def __init__(self, id, description, priority, completed=False, tags=None):
        super().__init__(id, description, completed, tags)
        self.priority = priority

    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        data["_type"] = "PriorityTask"
        return data

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Priority: {self.priority}"