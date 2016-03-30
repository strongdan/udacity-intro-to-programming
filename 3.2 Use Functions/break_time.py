# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
import webbrowser
import time

total_breaks = 3
break_count = 0

while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1
    
# Your code here.