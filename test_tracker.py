"""
Name: Michael Ko
Project Name: Weekly_Exercise_Tracker (test_tracker.py)
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/04/2026
Purpose: pytest tests. Testing the ExerciseLog class. 
Starter Code: Chapter 11 of the Python Crash Course Textbook. Used the textbook as well as outside sources (websites) to learn more abot topics covered in textbook. 
Note: I used the following source to help with creating the test function(s) for NameStore: 
- https://docs.pytest.org/en/stable/how-to/tmp_path.html
"""
import pytest

from tracker import ExerciseLog, NameStore

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

def test_save_and_load_name(tmp_path):
    """A saved name loads back the same."""
    path = tmp_path / "name.json"
    NameStore(path).set_name("Michael")
    assert NameStore(path).name == "Michael"

def test_load_name_missing_file(tmp_path):
    """No saved file means no name."""
    assert NameStore(tmp_path / "missing.json").name is None