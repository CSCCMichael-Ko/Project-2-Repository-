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

    def add_exercise(self, name, reps):
        """Add reps to a total. True if added, False if reps is below 1."""
        if reps < 1:
            return False
        self.totals[name] = self.totals.get(name, 0) + reps
        return True