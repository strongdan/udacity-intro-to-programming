# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
import os, sys
saved_path = os.getcwd()


def rename_files():
    #get filenames
    os.chdir(r"F:\Projects\Udacity_Programming\3.2 Use Functions\Secret_Message")
    file_list = os.listdir(r"F:\Projects\Udacity_Programming\3.2 Use Functions\Secret_Message")
    for file_name in file_list:
        #rename each file, removing numbers
        print file_name
        os.rename(file_name, file_name.translate(None, '0123456789'))
        print file_name
rename_files()

# Your code here.