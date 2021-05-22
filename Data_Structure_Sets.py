# Sets are data structure in python in which elements are unordered as well as unindexed
# Unordered elements means that elements appear in random order and unindexed means that elements do not have specific address
# to eventually call them. As there is no specific index of element in a set so they cannot be called individually

# In order to declare a set a number of elements are written in curly brackets
# For example
its_set = {'january','february','march','april','may','june','july','august','september','october','november','december'}
print(its_set)                                                              # Prints the entire set named its_set

# Two separate sets are declared in order to perform test different methods of sets in python
set1 = {'book','pencil','notebook','eraser','sharpner','ruler'}             # Declares a set named set1
set2 = {'notebook','ballpoint','ruler','book','marker'}                     # Declares a set named set2
print(set1)                                                                 # Prints entire set1
print(set2)                                                                 # Prints all elements in set2
set1.add('lunchbox')                                                        # Adds "lunchbox" as element in set1
set2.update(['tiffon','pen'])                                               # Adds "tiffon? and "pen" as element in set2
print(set1)                                                                 # Prints all elements of set1
print(set2)                                                                 # Prints all elements of set2
length_of_set1 = len(set1)                                                  # Gets length of set1 and store it in variable named
                                                                            # length_of_set1
length_of_set2 = len(set2)                                                  # Gets length of set2 and store it in variable named
                                                                            # length_of_set2
print(length_of_set1)                                                       # Prints value stored in variable length_of_set1
print(length_of_set2)                                                       # Prints value stored in variable length_of_set2
its_set.remove('january')                                                   # Remmoves element "january" from its_set
print(its_set)                                                              # Prints its_set from which january was previously removed
its_set.add('january')                                                      # Adds element "january" in its_set
its_set.discard('march')                                                    # Removes element "march" from its_set
print(its_set)                                                              # Prints all element in its_set
its_set.add('march')                                                        # Adds element "march" in its_set
removed_item = its_set.pop()                                                # Removes the last element of the set
print(removed_item)                                                         # Prints the element which is removed using .pop() method
its_set.add(removed_item)                                                   # Add whatever is stored in removed_item variable to the
                                                                            # set named its_set
print(its_set)                                                              # Prints all elements of its_set
its_set.clear()                                                             # Removes all the elements stroed in its_seet
print(its_set)                                                              # Prints its_set which shows null value
del its_set                                                                 # Deletes set named its_set
list = ['this','is','a','list','in','python']                               # Declares a list named list
make_it_set = set(list)                                                     # Makes a set named make_it_set from given list
print('this set is converted from the list' , make_it_set)                  # Print all elements of newly made set
print('difference of two sets is' , set1.difference(set2))                  # Print all elemens that are present in set1 but not in set2
print('difference of set 2 and set1 is',set2.difference(set1))              # Prints all elements that are present in set2 but not in set1
# set1.difference_update(set2)                                              # Checks the common elements in two sets and remove then
                                                                            # from first set
# print(set1)                                                               # Prints set1 from which elements are just removed
print('intersection of two sets is',set1.intersection(set2))                # Prints all elements that are common in two sets
# set1.intersection_update(set2)                                            # Gets common elements in two sets and stored them
                                                                            # in first set
# print(set1)                                                               # Prints set1 which contains common elements to two sets
print('union of two sets is',set1.union(set2))                              # Prints all the elements of two sets
print('Whether sets are disjoint?',set1.isdisjoint(set2))                   # Prints false because sets do not have intersection
print('Whether sets are subsets?',set1.issubset(set2))                      # Prints false because set2 is not subset of set1
print('Whether sets are superset?',set1.issuperset(set2))                   # Prints false because set2 is not subset of set1
print('symmetric difference of sets is',set1.symmetric_difference(set2))    # Prints all elements that are not common in both sets
print(set1.symmetric_difference_update(set2))                               # Gets all elements that are common and remove them from
                                                                            # first set