# For loop in python is not like a For loop in any other programming language. In python for loop act as an item picker from a given
# number of item one at a time. It is just like picking a fruit from a basket one at a time.
# A for loop is declared by giving it a variable and a number of item to check from. For loop picks first item from given items and
# store it in variable. It then execute all the statements in its structure and then pick second item, store it in variable and
# execute all statements. It goes on like this until all the items are picked once.
# For example

car = ('body','wheel','lights','doors','seats','steering','dashboard')
for parts in car:                                       # Collect values of tuple one by one and store it in parts
    print("This car has a",parts)                       # Prints statements given in paranthesis

# Sometimes instead of a number of items, a string is given to a for loop. In this condition, for loop will get one character of that
# string and store it in variable. It then executes all its statements. This is done for all the characters in the string.
# For example

for char in "Sentence":                                 # Collects character of string "Sentence" one by one and store it in char
    print("String has character",char)                  # Prints statements given in paranthesis

# range() method is used to return a number of integers. It starts with integer 0 and increment it by 1. This continues until count
# reaches the value given in the paranthesis. It should be kept it mind that for will not get the number given in paranthesis but
# will stop at one number before that number.
# For example

for number in range(10):                                # Checks if number is below 10, store that value in number variable
    print("Number =",number)                            # Prints statements given in paranthesis

# If it is required to start and stop the count at specific values, start and stop values are given in paranthesis separated by
# comma. For statement will start the count at first value and stop it at second value.
# For example

for num in range(5,9):                                  # Checks if num is 5 or more and less than 9, store it in num
    print(num)                                          # Prints value of num

# If it is required that increment value should be other than 1 then 3 values are written in the paranthesis. First value represents
# starting point, second value represents ending point and third value represent the increment value. All three values are separated
# by comma.
# For example

for table in range(2,21,2):                             # Checks if table is in range from 2 to 20 and increment it by 2
    print("Table of 2 has",table)                       # Prints statements given in paranthesis