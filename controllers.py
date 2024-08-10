from models import Task, task_types
from datetime import datetime
from storage import TaskStorage

class TaskController:
    """
    Manages the business logic for handling tasks in the to-do list application.
    
    Methods:
        __init__(): Initializes the TaskController with a TaskStorage instance and loads existing tasks.
        add_task(name, task_type, date_str, urgency): Adds a new task to the list and saves it to storage.
        remove_task(index): Removes a task from the list based on its index and updates storage.
        get_tasks(): Retrieves the current list of tasks.
        get_task_types(): Retrieves the list of predefined task types.
    """
    
    def __init__(self):
        """
        Initializes the TaskController with a TaskStorage instance and loads existing tasks.
        """
        self.storage = TaskStorage()
        self.tasks = self.storage.load_tasks()

    def add_task(self, name, task_type, date_str, urgency):
        """
        Adds a new task to the list and saves it to storage.
        
        Args:
            name (str): The name or description of the task.
            task_type (str): The type or category of the task.
            date_str (str): The due date of the task in 'YYYY-MM-DD' format.
            urgency (str): The urgency level of the task.
        """
        date = datetime.strptime(date_str, '%Y-%m-%d')
        new_task = Task(name, task_type, date, urgency)
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)

    def remove_task(self, index):
        """
        Removes a task from the list based on its index and updates storage.
        
        Args:
            index (int): The index of the task to remove.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.storage.save_tasks(self.tasks)

    def get_tasks(self):
        """
        Retrieves the current list of tasks.
        
        Returns:
            list: The list of current tasks.
        """
        return self.tasks

    def get_task_types(self):
        """
        Retrieves the list of predefined task types.
        
        Returns:
            list: The list of predefined task types.
        """
        return task_types
