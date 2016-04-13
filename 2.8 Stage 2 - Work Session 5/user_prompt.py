blanks = ["___1___", "___2___", "___3___", "___4___"]

# - Level 0 Text - Easy
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

sample_answers = ['function', 'variables', 'outputs', 'lists']

# Level 1 Text - Moderate
lvl_1 = '''If you do need to iterate over a sequence of numbers, the built-in function ___1___
comes in handy. It generates arithmetic progressions. The given end point is never part of the
generated sequence; ___1___(10) generates 10 values, the legal indices for items of a sequence
of length 10. It is possible to let the ___1___ start at another number, or to specify a different
increment (even negative; sometimes this is called the ‘step’). To iterate over the indices of a
sequence, you can combine ___1___() and ___2___(). In most such cases, however, it is convenient
to use the ___3___() function. In many ways the object returned by ___1___() behaves as if it is
a list, but in fact it isn’t. It is an object which returns the successive items of the desired
sequence when you iterate over it, but it doesn’t really make the list, thus saving space. We say
such an object is ___4___, that is, suitable as a target for functions and constructs that expect
something from which they can obtain successive items until the supply is exhausted.'''

lvl1_answers = ['range', 'len', 'enumerate', 'iterable']

# Level 2 Text - Hard
lvl_2 = '''The ___1___ statement breaks out of the smallest enclosing for or while loop.
Loop statements may have an else clause; it is executed when the loop terminates through
exhaustion of the list (with for) or when the condition becomes false (with while), but
not when the loop is terminated by a ___1___ statement. The ___2___ statement in Python
returns the control to the beginning of the while loop. The ___2___ statement rejects all the
remaining statements in the current iteration of the loop and moves the control back to the
top of the loop. The ___3___ statement does nothing. It can be used when a statement is
required syntactically but the program requires no action.Another place ___3___ can be
used is as a place-holder for a function or conditional body when you are working on new code,
allowing you to keep thinking at a more abstract level. If the ___4___ statement is used with a
for loop, the ___4___ statement is executed when the loop has exhausted iterating the list.
If the ___4___ statement is used with a while loop, the ___4___ statement is executed when
the condition becomes false.'''

lvl2_answers = ['break', 'pass', 'continue', 'else']

# Level 3 Text - Harder
lvl_3 = '''Small anonymous functions can be created with the ___1___ keyword. This function
returns the sum of its two arguments: ___1___ a, b: a+b. ___1___ functions can be used wherever
function objects are required. They are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for a normal function definition. Like nested
function definitions, ___1___ functions can reference variables from the containing scope:
___2___ operations are operations that directly manipulate bits. List ___3___s provide
a concise way to create lists. Common applications are to make new lists where each element is
the result of some operations applied to each member of another sequence or iterable, or to
create a subsequence of those elements that satisfy a certain condition. A tuple is a sequence
of immutable Python objects. ___4___s are sequences, just like lists. The differences between
___4___s and lists are, the ___4___s cannot be changed unlike lists and ___1___s use parentheses,
whereas lists use square brackets.'''

lvl3_answers = ['lambda', 'bitwise', 'comprehension', 'tuple']

def user_lvl():
    # user first selects a level
    user_in = int(input("Please select a level from 0 to 3:  ))

    # prompt a user with a sentence containing several blanks
    # The user should then be asked to fill in each blank appropriately to complete the sentence                   
    if user_in == 0
        w1, w2, w3, w4 = input("Please type a word for each of the blanks above, separated by spaces.\n" + sample + '\n\nWords: ').split() 
    elif user_in == 1
        w1, w2, w3, w4 = input("Please type a word for each of the blanks above, separated by spaces.\n" + lvl_1 + '\n\nWords: ').split() 
    elif user_in == 2
        w1, w2, w3, w4 = input("Please type a word for each of the blanks above, separated by spaces.\n" + lvl_2 + '\n\nWords: ').split()
    elif:
        w1, w2, w3, w4 = input("Please type a word for each of the blanks above, separated by spaces.\n" + lvl_3 + '\n\nWords: ').split() 
    else:
        break
                    
print(w1, w2, w3, w4)
