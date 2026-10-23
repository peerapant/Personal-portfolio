import datetime
from src.task import Task, DueDateTask, PriorityTask
from src.data_persistence import DataPersistence

class TaskManager:
    PRIORITY_MAP = {"High": 1, "Medium": 2, "Low": 3}

    def __init__(self, filepath="data/tasks.json"):
        self.persistence = DataPersistence(filepath)
        self.tasks = self.persistence.load_tasks()

    def _get_next_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def _save(self):
        self.persistence.save_tasks(self.tasks)

    # --- Basic Operations ---
    def add_normal_task(self, description, tags=None):
        task = Task(self._get_next_id(), description, tags=tags)
        self.tasks.append(task)
        self._save()
        return task

    def add_due_date_task(self, description, due_date_str, tags=None):
        try:
            task = DueDateTask(self._get_next_id(), description, due_date_str, tags=tags)
            self.tasks.append(task)
            self._save()
            return task
        except ValueError:
            return None

    def add_priority_task(self, description, priority, tags=None):
        if priority not in ["High", "Medium", "Low"]:
            return None
        task = PriorityTask(self._get_next_id(), description, priority, tags=tags)
        self.tasks.append(task)
        self._save()
        return task

    def get_all_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self._save()
                return True
        return False

    def delete_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        if len(self.tasks) < initial_count:
            self._save()
            return True
        return False

    # --- Search / Filter / Sort ---
    def search_tasks(self, keyword):
        kw = keyword.lower()
        results = []
        for task in self.tasks:
            in_desc = kw in task.description.lower()
            in_tags = any(kw in tag.lower() for tag in task.tags)
            if in_desc or in_tags:
                results.append(task)
        return results

    def filter_tasks(self, status=None, priority=None, tag=None):
        result = self.tasks
        if status is not None:
            result = [t for t in result if t.completed == status]
        if priority:
            result = [t for t in result if isinstance(t, PriorityTask) and t.priority == priority]
        if tag:
            result = [t for t in result if tag.lower() in [t_tag.lower() for t_tag in t.tags]]
        return result

    def sort_tasks(self, criterion="id", reverse=False):
        result = list(self.tasks)
        if criterion == "description":
            result.sort(key=lambda t: t.description.lower(), reverse=reverse)
        elif criterion == "completed":
            result.sort(key=lambda t: t.completed, reverse=reverse)
        elif criterion == "priority":
            result.sort(
                key=lambda t: self.PRIORITY_MAP.get(t.priority, 99) if isinstance(t, PriorityTask) else 99,
                reverse=reverse
            )
        else:
            result.sort(key=lambda t: t.id, reverse=reverse)
        return result