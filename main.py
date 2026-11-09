"""
Name: Michael Ko
File Name: main.py
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/04/2026
Purpose: main.py handles everything the user sees and imports the class from tracker.py
Starter Code: Used the textbook as well as outside sources (websites) to learn more abot topics covered in textbook. 
"""

from tracker import ExerciseLog, NameStore

def ask_whole_number(prompt):
    """Function that asks until the user types a whole number greater than 0."""
    text = input(prompt)
    while not text.isdigit() or int(text) == 0:
        print("Please enter a whole number greater than 0.")
        text = input(prompt)
    return int(text)

def get_user_name(store):
    """Return the saved name, or ask for one and save it for next time."""
    if store.name:
        print(f"Welcome back, {store.name}!")
        return store.name
    name = input("What is your name? ").strip()
    while name == "":
        print("Please enter your name.")
        name = input("What is your name? ").strip()
    store.set_name(name)
    print(f"We'll remember you when you come back, {name}!")
    return name

def ask_goals(log):
    """Ask for this week's goals and store them in the log."""
    exercise_goal = ask_whole_number("Goal (Exercises This Week): ")
    reps_goal = ask_whole_number("Goal (Reps Per Exercise): ")
    log.set_goals(exercise_goal, reps_goal)

def log_exercises(log):
    """Keep asking for exercises and reps until the user types 'q'."""
    while True:
        exercise = input("\nExercise name ('q' to quit): ").strip()
        if exercise == "q":
            break
        if exercise == "":
            print("Please enter an exercise name.")
            continue
        log.add_exercise(exercise, ask_whole_number("Number of Reps: "))

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
    get_user_name(NameStore())
    log = ExerciseLog()
    ask_goals(log)
    log_exercises(log)
    show_totals(log)

if __name__ == "__main__":
    main()