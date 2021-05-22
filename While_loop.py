# While loop is used to run a specific number of line as long as condition given in while loop is true
# The number of time a while loop run is indefinite means it is not known how many times a while loop will execute
# A while loop may execute given lines for once or infinite times

# To define a while loop, a variable list, set, tuple, dictionary etc. is defined. While statement is defined which checks a specific
# condition. This condition may use comparator operator or check whether an element is present in set, list, tuple, class etc.
# The value of the element to be checked should change in a loop or else loop will continue forever.
# For example

# Defining a variable and using comparator operator to execute a while loop
num = 10                                                    # Defines a variable named num and assigns it integer 10
while num != 0:                                             # Checks whether num is equal to 0 or not
    print("While loop is still operating")                  # Prints a message "While loop is still operating"
    num=num-1                                               # Decreases value of num by 1
print("While loop is not executing anymore")                # Prints a message "While loop is not executing anymore"

# Defining a data structure and checking whether an element exists in data structure or not
list = [1,2,3,4,5,6,7,8,9,10]                               # Defines a list with integer from 1 to 10
num = 1                                                     # Redefines num and assigns it integer 1
while num in list:                                          # Checks whether num exists in list
    print("Number exists in the list")                      # Prints a message "Number exists in the list"
    num = num+1                                             # Increments value of num by 1
print("Number is not in list anymore")                      # Prints a message "Number is not in list anymore"

# Defining data structure by using string data type and checking condition using while loop
basket = ['apple','banana','mango','pear','grapes','strawberry','guava','melon','orange']
                                                            # Defines a list named basket and assigns it fruit names as elements
fruit = input("Enter your fruit's name ")                   # Asks user for input and stores it in variable named fruit
while fruit in basket:                                      # Checks whether value of fruit is in list named basket
    print("Your fruit is in the basket")                    # Prints a message "Your fruit is in the basket"
    fruit = input("Enter your fruit's name again")          # Asks user for input and stores it in variable named fruit
print("your fruit is not in the basket")                    # Prints a message "your fruit is not in the basket"