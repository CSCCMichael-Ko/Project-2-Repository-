"""
Name: Michael Ko
File Name: tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/03/2026
Purpose:
Starter Code: None
"""

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