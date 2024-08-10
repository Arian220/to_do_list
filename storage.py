import csv
from models import Task
from datetime import datetime

class TaskStorage:
    """
    Manages saving and loading tasks to and from a CSV file.

    Attributes:
        filename (str): The name of the CSV file where tasks are stored. Defaults to 'tasks.csv'.

    Methods:
        __init__(filename='tasks.csv'): Initializes the TaskStorage with a specified file name.
        save_tasks(tasks): Saves a list of tasks to the CSV file.
        load_tasks(): Loads tasks from the CSV file and returns them as a list of Task objects.
    """
    
    def __init__(self, filename='tasks.csv'):
        """
        Initializes the TaskStorage with a specified file name.
        
        Args:
            filename (str): The name of the CSV file where tasks will be stored.
        """
        self.filename = filename

    def save_tasks(self, tasks):
        """
        Saves a list of tasks to the CSV file.
        
        Args:
            tasks (list): A list of Task objects to be saved.
        """
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'task_type', 'date', 'urgency', 'color'])
            for task in tasks:
                writer.writerow([task.name, task.task_type, task.date.strftime('%Y-%m-%d'), task.urgency, task.color])

    def load_tasks(self):
        """
        Loads tasks from the CSV file and returns them as a list of Task objects.
        
        Returns:
            list: A list of Task objects loaded from the CSV file. If the file does not exist, returns an empty list.
        """
        tasks = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(
                        name=row['name'],
                        task_type=row['task_type'],
                        date=datetime.strptime(row['date'], '%Y-%m-%d'),  # Convert string to datetime
                        urgency=row['urgency']
                    )
                    tasks.append(task)
        except FileNotFoundError:
            pass  # If the file does not exist, simply return an empty list
        return tasks
