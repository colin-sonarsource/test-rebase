# This Python code intentionally contains issues that SonarQube would flag.

import os

def bad_function():
    password = "hardcoded_password"  # Sensitive data hardcoded
    print("This is a debug message")  # Debug message left in code
    os.system("ls -l")  # Use of os.system instead of subprocess (security risk)
    x = 1 / 0  # Division by zero
    eval("print('Hello World')")  # Use of eval (security risk)
    return

def third_bad_function():
    password = "hardcoded_password"  # Sensitive data hardcoded
    print("This is a debug message")  # Debug message left in code
    os.system("ls -l")  # Use of os.system instead of subprocess (security risk)
    x = 1 / 0  # Division by zero
    eval("print('Hello World')")  # Use of eval (security risk)
    return

bad_function()
third_bad_function()
