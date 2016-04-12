# prompt a user with a sentence containing several blanks
# The user should then be asked to fill in each blank appropriately to complete the sentence

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

w1, w2, w3, w4 = input("Please type a word for each of the blanks above.\n" + sample + '\n\nWords: ').split()

print(w1, w2, w3, w4)
