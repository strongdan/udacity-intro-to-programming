# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# Add your own code and notes here

def find_element(lst, val):
    if val in lst:
        return lst.index(val)
    elif val not in lst:
        return -1
        
    #output index of list element
