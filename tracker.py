"""
Name: Michael Ko
File Name: tracker.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/03/2026
Purpose:
Starter Code: None
"""

log = {}

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

    if exercise in log:
        log[exercise] += reps
    else:
        log[exercise] = reps

print("\nThis week's totals:")
for exercise in log:
    print(f"{exercise}: {log[exercise]} reps")