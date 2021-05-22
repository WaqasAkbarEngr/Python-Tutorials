# List is a type of data strucutre which has ordered elements and can be changed
# List may contain duplicate elements means that two or more elements with same name may exist
# To define a List it is written in a square bracket "[]"

first_list = [ 'first' , 'second' , 'third' , 'fourth' , 'fifth' ]  #List named first_list is defined here
print ( first_list )                                                # Printing List named first_list

print( len(first_list) )                                            # Prints length of List using method "len()"

# In order to print a single entry of the List, put a square bracket at the end of variable name and insert index number
# in it i.e. first_list[index]. The index of the List elements is off by 1 means that index value if 1 less than the number
# of element. For example, index number of first element is 0
print ( first_list[0] )                                             # Prints first entry of the List
print ( first_list[1] )                                             # Prints second entry of the List
print ( first_list[2] )                                             # Prints third entry of the List
print ( first_list[3] )                                             # Prints fourth entry of the List
print ( first_list[4] )                                             # Prints fifth entry of the List
print ( first_list )                                                # Print the entire List

# As elements of a List are changabel, so assigning a new value by using assignment operator changes the old value by the
# new value. Index number is used to change the value of specific element
# For example
first_list[0] = 'third'                                             # Changes the first entry and replace it by value "third"
first_list[2] = 'second'                                            # Changes the third entry of list and replace it  by "second"
first_list[4] = 'first'                                             # Changes the fifth entry of list and replace it by "first"
print (first_list)                                                  # Print the entire List with new values

# Append() method is used to entre a new element at the end of the List
# For example
first_list.append("sixth")                                          # Add a new element "sixth" at the end of the List
print( first_list )                                                 # Prints the entire List with six elements

# Insert() method is used to insert a new element at the specified index in the List. It is used when element is to be entered
# at a specific position instead of at the end of the List
# For example
first_list.insert(2, "inserted")                                    # Inserts element "inserted" at index 2 or position 3
print(first_list)                                                   # Prints entire List with newly inserted element

# Remove() method is used to remove an element from the List. The element to be removed is given in the paranthesis as an argument
# For example
first_list.remove('second')
print(first_list)

first_list = [ 'first' , 'second' , 'third' , 'fourth' , 'fifth' ]  #List named first_list is redefined here to rectify the effect
                                                                    # of remove() method in last statemnet

# Pop() method also remove an element from the List. Index number of element to be removed is given as an argument. If no argument is
# given pop() removes the element with last index number
# For example
first_list.pop(3)                                                   # Removes element with index number 3
print(first_list)                                                   # Prints entire List with element on index 3 removed
first_list.pop()                                                    # Removes last element of the List
print(first_list)                                                   # Prints List with last element removed

first_list = [ 'first' , 'second' , 'third' , 'fourth' , 'fifth' ]  #List named first_list is redefined here to rectify the effect
                                                                    # of pop() method in last statemnet

# Del() also removes an element with index number given in paranthesis as an argument. In case no argument is given, del() removes
# the entire list
For example
del first_list[4]                                                   # Removes element with index number 4
print(first_list)                                                   # Prints List after removing element with index number 4
del() first_list                                                    # Removes the entire List
print(first_list)                                                   # Gives error because List named "first_list" does not exist

first_list = [ 'first' , 'second' , 'third' , 'fourth' , 'fifth' ]  #List named first_list is redefined here because it was removed

# Clear() is used to remove all the element of the List but List still exists and it is empty
# For example
first_list.clear()                                                  # Clears the list named "first_list"
print(first_list)                                                   # Print List and it is empty

first_list = [ 'first' , 'second' , 'third' , 'fourth' , 'fifth' ]  #List named first_list is redefined here to rectify the effect
                                                                    # of clear() method in last statemnet

# copy() method copy the entire List and store it in another List by use of assignment operator
# For example
second_list = first_list.copy()                                     # Copies List named "first_list" and all of its content and
                                                                    # store it in List named "second_list"
print(second_list)                                                  # Prints entire List named "second_list"

# count() method is used to count the number of time an element is present in a List. It means if an element is present in a List
# two times then count() will return value 2
# For example
count = second_list.count('second')                                 # Counts number of occurance of element "second" in the list
                                                                    # named second_list
print(count)                                                        # Prints the value stored in variable named count

# extend() method adds all the elements of a list given in paranthesis as argument to specified list. The elements are added at the end
# of the list and the list retains its own elements. It simply means that specified list is increased by the element of the list given
# as an argument to extend() method
# For example
first_list.extend(second_list)                                      # adds all elements of second_list to first_list
print(first_list)                                                   # Prints the List named as first_list

# index() method gives the index of the element given in the paranthesis as an argument.
# For example
index = first_list.index('second')                                  # gets index of "second" from list and store in variable named index
print(index)                                                        # Print the value of variable index

# reverse() method reverses the order of the elements of specified list.
# For example
second_list.reverse()                                               # reverses the order of elements of second_list
print(second_list)                                                  # print second_list whose elements are reversed

# sort() method arrange the elements of the list in alphabetical order.
# For example
second_list.sort()                                                  # sorts the elements of the list named second_list
print(second_list)                                                  # Print second_list whose element are sorted