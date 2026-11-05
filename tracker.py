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

log = ExerciseLog()

while True:
    exercise = input("\nExercise name ('q' to quit): ").lower()
    if exercise == "q":
        break
    if exercise == "":
        print("Please enter an exercise name.")
        continue

    reps = input("Reps done: ")
    while not reps.isdigit() or int(reps) == 0:
        print("Please enter a whole number greater than 0.")
        reps = input("Reps done: ")
    reps = int(reps)

    log.add_exercise(exercise, reps)

print("\nThis week's totals:")
for exercise in log.totals:
    print(f"{exercise}: {log.totals[exercise]} reps")