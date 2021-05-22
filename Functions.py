# Sometimes you have to use some statements over and over again in order to complete the task at hand
# This can be make simple by use of functions. Funcetion is a set of instruction that perform a specific task.
# Function should be defined before first and are called where needed
# Following is a simple function that accepts no argument and returns no value. It just print different statements.
def function ():                                # Defines a function named function
    print("You called me, MY LORD!!!!")         # Prints a statement
    print("This statement is in function")      # Prints a statement
    print("This is the end of your function")   # Prints a statement

function()                                      # Calls function named function and run all its indented statements

# Following function accepts a numeric value as argument and return its square.
def square(number):                             # Defines a function named square with parameter number which should be integer
    squ = number*number                         # Multiply number with itself and store it in variable squ
    return squ                                  # Returns the value stored in squ

print("The square of number is",square(8))      # Calls function named square and prints whatever value it returns

# Following function accepts a string value and perform different operation on it
def string_function (name):                     # Defines a function named string_function with name as parameter which should be string
    print("Your name is", name)                 # Prints "Your name is" along with value stored in variable name

string_function("Waqas")                        # Calls the function named string_function

# When parameters are given in function and it is required to define a default parameter, in case there is no parameter given
# during call of function. In such a case, parameter given in function definition is assigned a default string value which is
# returned when no parameter is given during function call
def default_function(default = "Default"):      # Defines a function named default_function having parameter with a default value
    print("You entered",default)                # Prints statement given in paranthesis

default_function()                              # Calls function without any parameter and uses default value
default_function("'This is a function'")        # Calls function with parameter given and uses this parameter

# Sometimes a function is defined without any name. These functions are called anonymous function and mostly also known as Lambda
# function. These functions do not require def keyword to define them but instead use lambda keyword. Like any other function they
# must be defined first and called when needed. To define a Lambda function first give it a function name followed by assignment
# operator. Then write keyword lambda with or without parameters (separated by commas if more than one). Then give a colon sign and
# write expresssion of the task that this lambda function has to perform. A lambda function is only one line statement mean it does
# not have any indented line
# For example

sum = lambda first,second: first + second

answer = sum(12,15)
print(answer)

# A lambda function may also contain print statement
# For example

intro = lambda : print("My name is Lambda Function")

intro()

# A lambda function also deals with string type parameters
# For example

full_name = lambda first_name,second_name: print("I am",first_name,second_name)
full_name("Lambda","Function")