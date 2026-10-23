import sys
import os

# เพิ่มโฟลเดอร์ src เข้าใน Python Path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from task_manager import TaskManager
from cli_interface import CLIInterface

def main():
    manager = TaskManager()
    cli = CLIInterface(manager)
    cli.run()

if __name__ == "__main__":
    main()