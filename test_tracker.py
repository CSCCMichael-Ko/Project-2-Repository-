"""
Name: Michael Ko
Project Name: Weekly_Exercise_Tracker (test_tracker.py)
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/05/2026
Purpose: pytest tests
Starter Code: Chapter 11 of the Python Crash Course Textbook
"""
import pytest

from tracker import ExerciseLog, load_name, save_name

def test_add_exercise_starts_a_new_total():
    """The first time an exercise is logged, its total is the reps given."""
    log = ExerciseLog()
    added = log.add_exercise("push-ups", 20)
    assert added is True
    assert log.totals == {"push-ups": 20}

def test_add_exercise_adds_to_an_existing_total():
    """Logging the same exercise again adds to its total."""
    log = ExerciseLog()
    log.add_exercise("push-ups", 20)
    log.add_exercise("push-ups", 10)
    assert log.totals["push-ups"] == 30