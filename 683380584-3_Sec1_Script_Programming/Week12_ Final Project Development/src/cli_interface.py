class CLIInterface:
    def __init__(self, task_manager):
        self.manager = task_manager

    def display_menu(self):
        print("\n=== Task Manager ===")
        print("1. Add Normal Task")
        print("2. Add Due Date Task")
        print("3. Add Priority Task")
        print("4. List All Tasks")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Search Tasks")
        print("8. Filter Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        print("====================")

    def _get_tags_input(self):
        tags_raw = input("Enter tags (comma separated, press Enter to skip): ").strip()
        if not tags_raw:
            return []
        return [t.strip().lower() for t in tags_raw.split(",") if t.strip()]

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (0-9): ").strip()

            if choice == "1":
                desc = input("Task Description: ").strip()
                tags = self._get_tags_input()
                task = self.manager.add_normal_task(desc, tags)
                print(f"Added: {task}")

            elif choice == "2":
                desc = input("Task Description: ").strip()
                date_str = input("Due Date (YYYY-MM-DD): ").strip()
                tags = self._get_tags_input()
                task = self.manager.add_due_date_task(desc, date_str, tags)
                if task:
                    print(f"Added: {task}")
                else:
                    print("Invalid date format!")

            elif choice == "3":
                desc = input("Task Description: ").strip()
                prio = input("Priority (High/Medium/Low): ").strip().capitalize()
                tags = self._get_tags_input()
                task = self.manager.add_priority_task(desc, prio, tags)
                if task:
                    print(f"Added: {task}")
                else:
                    print("Invalid priority input!")

            elif choice == "4":
                tasks = self.manager.get_all_tasks()
                print("\n--- All Tasks ---")
                for t in tasks:
                    print(t)

            elif choice == "5":
                try:
                    task_id = int(input("Enter Task ID to complete: "))
                    if self.manager.complete_task(task_id):
                        print("Task completed!")
                    else:
                        print("Task not found.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "6":
                try:
                    task_id = int(input("Enter Task ID to delete: "))
                    if self.manager.delete_task(task_id):
                        print("Task deleted!")
                    else:
                        print("Task not found.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "7":
                kw = input("Enter keyword to search: ").strip()
                results = self.manager.search_tasks(kw)
                print(f"\n--- Search Results for '{kw}' ---")
                for t in results:
                    print(t)

            elif choice == "8":
                prio = input("Filter by Priority (High/Medium/Low, or Enter to skip): ").strip().capitalize()
                tag = input("Filter by Tag (or Enter to skip): ").strip()
                results = self.manager.filter_tasks(priority=prio if prio else None, tag=tag if tag else None)
                print("\n--- Filtered Tasks ---")
                for t in results:
                    print(t)

            elif choice == "9":
                crit = input("Sort by (id, description, completed, priority): ").strip().lower()
                results = self.manager.sort_tasks(criterion=crit if crit else "id")
                print("\n--- Sorted Tasks ---")
                for t in results:
                    print(t)

            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")