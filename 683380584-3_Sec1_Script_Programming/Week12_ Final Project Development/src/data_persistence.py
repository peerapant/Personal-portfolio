import json
import os
from .task import Task, DueDateTask, PriorityTask

class DataPersistence:
    def __init__(self, filepath="data/tasks.json"):
        self.filepath = filepath

    def load_tasks(self):
        if not os.path.exists(self.filepath):
            return []
        
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                tasks = []
                for item in raw_data:
                    task_type = item.pop("_type", "Task")
                    item.setdefault("tags", [])
                    
                    if task_type == "DueDateTask":
                        tasks.append(DueDateTask(**item))
                    elif task_type == "PriorityTask":
                        tasks.append(PriorityTask(**item))
                    else:
                        tasks.append(Task(**item))
                return tasks
        except Exception:
            return []

    def save_tasks(self, tasks):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        data = [task.to_dict() for task in tasks]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)