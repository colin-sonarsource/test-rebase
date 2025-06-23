# This Python code intentionally contains issues that SonarQube would flag.

import os

def bad_function():
    password = "hardcoded_password"  # Sensitive data hardcoded
    print("This is a debug message")  # Debug message left in code
    os.system("ls -l")  # Use of os.system instead of subprocess (security risk)
    x = 1 / 0  # Division by zero
    eval("print('Hello World')")  # Use of eval (security risk)
    return

<<<<<<< HEAD
def third_bad_function():
=======
def another_bad_function():
>>>>>>> 5c0d5c3 (Update test.py)
    password = "hardcoded_password"  # Sensitive data hardcoded
    print("This is a debug message")  # Debug message left in code
    os.system("ls -l")  # Use of os.system instead of subprocess (security risk)
    x = 1 / 0  # Division by zero
    eval("print('Hello World')")  # Use of eval (security risk)
    return

bad_function()
<<<<<<< HEAD
third_bad_function()
=======
another_bad_function()
>>>>>>> 5c0d5c3 (Update test.py)
