from tracker import ExerciseLog

def ask_reps():
    """Function that asks until the user types a whole number greater than 0; return it."""
    reps = input("Reps done: ")
    while not reps.isdigit() or int(reps) == 0:
        print("Please enter a whole number greater than 0.")
        reps = input("Reps done: ")
    return int(reps)

def show_totals(log):
    """Print each exercise's total reps for the week."""
    print("\nThis week's totals:")
    for exercise in log.totals:
        print(f"{exercise}: {log.totals[exercise]} reps")

def main():
    """Log exercises until the user quits, then show the totals."""
    log = ExerciseLog()
    while True:
        exercise = input("\nExercise name ('q' to quit): ").strip()
        if exercise == "q":
            break
        if exercise == "":
            print("Please enter an exercise name.")
        log.add_exercise(exercise, ask_reps())
    show_totals(log)

if __name__ == "__main__":
    main()