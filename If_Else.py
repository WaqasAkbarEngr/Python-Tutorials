# One of the flow control statement is if_else statement. This statement shifts the flow of program to other lines on the program
# based on the outcome of conditions. It shifts control to next line if condition is true and ignore all indented lines of if_else
# when condition is false

# One way to write an if_else statement is by using comparator operator like 1<3 or 3>2 etc.
# The syntax is,
# if (expression):
#     (Statement)
# For example
weight = 50                                                         # Declares a variable named weight and assign it value 50
if weight < 60:                                                      # Checks if weight is less than 60
    print("underweight")                                            # Prints whatever is given in paranthesis

if weight > 100:                                                     # Checks if weight is more than 100
    print("overweight")                                             # Prints whatever is given in paranthesis

# else is used along with if statement when it is required to do two different task based on outcome of conditional check

# Sometimes task at hand is not achieved by a single if statement. For this purpose, more than one if statements are defined inside
# one another. This type of structure of if statement is called nested if statement structure.
# To build a nested if structure with n number of if statements, second to (n-1) if statement to be entered has letters "el" as
# prefixes i.e. elif. "el" is short of else, so elif can be read as else if, meaning if one condition returns false it checks
# whether other conditions are true or false. Nested if statements are executed in order and if one condition returns true, control
# is shifted out of nested if structure and all the other if statements are not checked.
# In a nested if statement structure, first if statement contains if (condition) and last if statement contains else (with
# no condition). All other if statements in the middle contains elif (condition)
num1 = 33                                                           # Declares a variable num1 and assign it integer 33
if num1 > 33:                                                       # Checks if num1 is greater than 33
    print("You are pass")                                           # Prints "You are pass" if above condition is true
elif num1 < 33:                                                     # Checks if num1 is less than 33 after first condition is false
    print("You are fail")                                           # Prints "Your are fail" if above condition is true
else:                                                               # Checks if all nested if_else are false then execute next line
    print("You got passing marks")                                  # Prints "You got passing marks"

# Another way to write an if_else statement is to check whether a value exists in a variable, set, tuple, list, dictionary, class etc.
# The syntax is,
# if (value) in (variable):
#   (statement)
# For example
school_bag = ('pencil','eraser','sharpner','notebook','stationary case')    # Declares list named school_bag
pencil = {'brand':'goldfish','type':'HB','size':2.5,'material':'wood'}      # Declares dictionary named pencil
geometry_set = {'ruler','compass','protector','triangles'}                  # Declares set named geometry_set
math_book = ['sets','number system','algebra','trignometry']                # Declares tuple named math_book
if "pencil" in school_bag:                                          # Checks if pencil is present in list "school_bag"
    print("Pencil is in school bag")                                # Prints this statement if pencil exists in school_bag
elif "book" in school_bag:                                          # Checks if book is present in list " school_bag"
    print("Book is in school bag")                                  # Prints this statement if book exists in school_bag

if 'brand' in pencil:                                               # Checks if key "brand" is present dictionary "pencil"
    print(pencil['brand'], "is your brand")                         # Prints this statement if key is present in dictionary
else:                                                               # Execute next statement provided above given if returns false
    print("you got it all wrong")                                   # Prints this statement when else is activated
if "ruler" in geometry_set:                                         # Checks if "ruler" is present in set "geometry_set"
    print("You got ruler in geometry set")                          # Prints this statement if ruler is in geometry_set
if "tables" in geometry_set:                                        # Checks if "tables" is present in set "geometry_set"
    print("There are tables")                                       # Prints this statement if tables is in geometry_set
else:                                                               # Activated when all above if statement returns false
    print("Table are not in your geometry set")                     # Prints this statement if else is activated
if "number system" in math_book:                                    # Checks if "number system" is present in tuple "math_book"
    print("Yes your math's book has number system")                 # Prints this statement if number system is present in math_book