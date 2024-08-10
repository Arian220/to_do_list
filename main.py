#!/usr/bin/env python3

"""
main.py

This is the entry point for the terminal-based to-do list application. It initializes the controller and view, and then starts the application.

Functions:
    main() -- Initializes the TaskController and TaskView, then starts the application.
"""

from controllers import TaskController
from views import TaskView

def main():
    """
    Initializes the TaskController and TaskView, then starts the application.
    """
    controller = TaskController()
    view = TaskView(controller)
    view.start()

if __name__ == "__main__":
    main()
