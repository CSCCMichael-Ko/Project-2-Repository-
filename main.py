"""
Name: Michael Ko
File Name: main.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/04/2026
Purpose: main.py handles everything the user sees and imports the class from tracker.py
Starter Code: Used the textbook as well as outside sources (websites) to learn more abot topics covered in textbook. 
"""

from tracker import ExerciseLog, load_name, save_name, name_file

def ask_whole_number(prompt):
    """Function that asks until the user types a whole number greater than 0."""
    text = input(prompt)
    while not text.isdigit() or int(text) == 0:
        print("Please enter a whole number greater than 0.")
        text = input(prompt)
    return int(text)

def set_goals(self, exercise_goal, reps_goal):
    """
    Set how many exercises to do this week and how many reps for each.
    Updates a boolean to True if goals are valid (at least 1), otherwise False.
    """
    if exercise_goal >= 1 and reps_goal >= 1:
        self.exercise_goal = exercise_goal
        self.reps_goal = reps_goal
        self.goals_are_set = True
    else:
        self.goals_are_set = False

def show_totals(log):
    """Print each exercise's total reps for the week."""
    print("\nThis week's totals:")
    for exercise in log.totals:
        line = f"{exercise}: {log.totals[exercise]} reps"
        if log.totals[exercise] >= log.reps_goal:
            line += " (Reps (Repetition) goal met)"
        print(line)
    print(f"\nExercises done: {len(log.totals)} of {log.exercise_goal}.")


def main():
    """Greet the user, ask for goals, log exercises until the user quits, then show progress."""
    name = load_name(name_file)
    if name:
        print(f"Welcome back, {name}!")
    else:
        name = input("What is your name? ").strip()
        while name == "":
            print("Please enter your name.")
            name = input("What is your name? ").strip()
        save_name(name, name_file)
        print(f"We'll remember you when you come back, {name}!")
    
    log = ExerciseLog()
    log.set_goals(
        ask_whole_number("Goal (Exercises This Week): "), ask_whole_number("Goal (Reps Per Exercise): ")
    )
    while True:
        exercise = input("\nExercise name ('q' to quit): ").strip()
        if exercise == "q":
            break
        if exercise == "":
            print("Please enter an exercise name.")
        log.add_exercise(exercise, ask_whole_number("Number of Reps: "))
    show_totals(log)

if __name__ == "__main__":
    main()