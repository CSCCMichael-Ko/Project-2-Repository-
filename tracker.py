"""
Name: Michael Ko
File Name: tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/03/2026
Purpose:
Starter Code: None
"""
from pathlib import Path
import json

name_file = Path("username.json")

class ExerciseLog:
    """Class stores the total reps done for each exercise (week)"""
    def __init__(self):
        """Starts with no exercises logged."""
        self.totals = {}
        self.exercise_goal = 0
        self.reps_goal = 0
        self.goals_are_set = False

    def add_exercise(self, name, reps):
        """Add reps to a total. True if added, False if reps is below 1."""
        if reps < 1:
            return False
        self.totals[name] = self.totals.get(name, 0) + reps
        return True

    def set_goals(self, exercise_goal, reps_goal):
        """Sets amount of exercises to do this week and how many reps for each.

        Raises ValueError if either goal is less than 1.
        """
        if exercise_goal < 1 or reps_goal < 1:
            raise ValueError("Goals must be at least 1.")
        self.exercise_goal = exercise_goal
        self.reps_goal = reps_goal

    def new_week(self):
        """Clears totals and goals for another/new week"""
        self.totals = {}
        self.exercise_goal = 0
        self.reps_goal = 0

def save_name(name, path):
    """Save the user's name to a JSON file."""
    contents = json.dumps(name)
    path.write_text(contents)
        
def load_name(path):
    """Return the saved name, or None if no name has been saved yet."""
    if path.exists():
        contents = path.read_text()
        name = json.loads(contents)
        return name
    else:
        return None