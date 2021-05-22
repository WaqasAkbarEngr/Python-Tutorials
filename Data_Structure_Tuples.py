# Tuple is a type of data structure which has ordered elements in it.
# The elements of a tuple cannot be changed after they are defined.
# A tuple may contain duplicate value in it, means there may be two or more same elements in a tuple

# In order to define a tuple, elements are written in a round bracket or paranthesis
my_tuple = ('apple','ball', 'cat', 'drum', 'egg')                       # Defines a tuple named my_tuple
print(my_tuple)                                                         # Print entire tuple named my_tuple

# In order to get a single element from the tuple, its index number is given as an argument in square bracket after tuple name
print(my_tuple[3])                                                      # Prints elements at index number 3 in tuple

# As tuple is unchangable, python returns an error when a value is assighed to tuple
# For example
# my_tuple[1] = "ant"                                                   # Gives an error about tuple not support assignment

# len() method is used to get the length of the tuple i.e. total number of elements in the tuple
# For example
length_of_my_tuple = len(my_tuple)                                      # Gets length of tuple and store it in variable named
                                                                        # length_of_my_tuple
print('Length of my tupel is' , length_of_my_tuple)                     # Print length of tuple which is stored in the variable
                                                                        # named length_of_my_tuple

# del method is used to delete entire tuple
# For example
del my_tuple                                                            # Deletes the entire tuple

my_tuple = ('apple','ball', 'cat', 'drum', 'egg')                       # Redefines tuple because del method deleted last tuple
print(my_tuple)                                                         # Print entire tuple named my_tuple

# tuple() method in python is used to convert any other data structure to tuple
# In this example, a list is defined and converted to tuple
list = ['apple','oragnes','mangoes','bananas']                          # Defines a list to convert it into tuple
convert_to_tuple = tuple(list)                                          # Converts the list into a tuple named convert_to_tuple
print(list)                                                             # Prints the entire list
print(convert_to_tuple)                                                 # Print tuple which is converted from list

# count() method in tuple is used to count the number of times an element is occured in a tuple
# For example
count = my_tuple.count('apple')                                         # Count the occurance of element "apple" in my_tuple

# index() method in tuple is used to check the index number of an element in a tuple
# For example
index = my_tuple.index('apple')                                         # Get the index number of element "apple" and store it
                                                                        # in variable named index
print(count)                                                            # Prints the value stored in count
print(index)                                                            # Print the value store in index