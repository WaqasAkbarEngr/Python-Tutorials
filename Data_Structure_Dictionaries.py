# Dictionary is a data structure in Python which is unordered and have index number. A dictionary has one or more items. Each item
# of dictionary consists of key and value. A key is similar to a variable and value is similar to constant value assigned to a
# variable. In other words each key has an assigned value.

# In order to declare a dictionary, items of a dictionary are written in curly brackets. Each item is separated by comma and in each
# item key and values are separated by colon.
# For example
laptop_dictionary ={"brand" : 'Acer','model' : 'Aspire','year bought': 2018}    # Declares a dictionary named laptop_dictionary
print(laptop_dictionary)                                                        # Print the dictionary named laptop_dictionary

# In order to get the type of a key of dictionary, type method is used where key is given as argument in square bracket after
# name of dictionary
# For example
print(type(laptop_dictionary['year bought']))                                   # Print the type of key named "year bought

# Dictionary declaration as discussed above
my_laptop = dict(brand = 'Acer', model = 'Aspire', year_bought = '2018')        # Make dictionary named my_laptop from given items
print(my_laptop)                                                                # Prints all items of my_laptop dictionary

# Giving a key as an argument in square bracket right after dictionary name will get value of that key
# For example
print(laptop_dictionary['brand'])                                               # Prints value of the key named "brand"
print(laptop_dictionary['model'])                                               # Prints value of the key named "model"
print(laptop_dictionary['year bought'])                                         # Prints value of the key named "year bought"

# The value of keys in a dictionary can be changed by using assignment operator. To assign a different value give key as argument in
# square brackets right after dictionary name and then type new value to be assigned after assinment operator
laptop_dictionary['year bought'] = 20018                                        # Changes value of the key named "year bought"
print(laptop_dictionary)                                                        # Prints all the keys of laptop_dictionary

# Checks type of dictionary as done before
print(type(laptop_dictionary['year bought']))                                   # Prints the type of key "year bought"

# Just like changing value of a key. A new item can be added in the dictionary. The name of new key is given in square bracket as
# an assignment after name of dictionary and value of that key is given after assignment operator
# For example
laptop_dictionary['colour'] = 'Black'                                           # Adds another key named "colour" with value  to
                                                                                # dictionary named laptop_dictionary
print(laptop_dictionary)                                                        # Prints all items of laptop_dictionary

# pop() method is used to remove an item from dictionary. Name of item to be removed is given in paranthesis as an argument
# For example
laptop_dictionary.pop("colour")                                                 # Removes key named "colour" and its value from
                                                                                # dictionary named laptop_dictionary
print(laptop_dictionary)                                                        # Prints all items of dictionary named laptop_dictionary

# del method completely deletes the entire dictionary
del my_laptop                                                                   # Deletes completes dictionary named my_laptop

# clear() method is used to delete all the items of a dictionary but dictionary itself is not deleted and it remains with no item in it.
# For example
laptop_dictionary.clear()                                                       # Clears all keys and their values but dictionary is
                                                                                # not removed
print(laptop_dictionary)                                                        # Prints laptop_dictionary which is empty

# Dictionary was deleted so it is redeclared below
laptop_dictionary ={"brand" : 'Acer','model' : 'Aspire','year bought': 2018}    # Assigns differnt keys and their values to dictionary
                                                                                # named laptop_dictionary

# copy method copies the entire dictionary and assign all of its items to another dictionary
# For example
copied_dictionary = laptop_dictionary.copy()                                    # Copies all the keys and their value of dictionary named
                                                                                # laptop_dictionary to copied_dictionary
print(copied_dictionary)                                                        # Prints all keys and value of copied_dictionary

# fromkeys() method is used to assign a specific value to every key of a dictionary and make a new dictionary from it
# For example
var = 123                                                                       # Declares variable "var" and assign it value "123"
print(dict.fromkeys(laptop_dictionary,var))                                     # Assign value of variable "var" to all the keys of
                                                                                # dictionary named laptop_dictionary

# get() method is used to fetch a specific item from dictionary. Simple give name of key of item to be fetched and get() will return
# its value
print(laptop_dictionary.get("model"))                                           # Gets a value of key named "model"

# items() method is used to get all the item of dictionary
print(laptop_dictionary.items())                                                # Prints all the items of laptop_dictionary

# keys() method is used to get keys of all items in a dictionary
print(laptop_dictionary.keys())                                                 # Prints all the keys of laptop_dictionary

# values() method is used to get values of all keys in a dictionary
print(laptop_dictionary.values())                                               # Prints all the values of laptop_dictionary

# Entering a few new items in the dictionary using above described procedure
laptop_dictionary['colour'] = 'black'                                           # Adds a new key named "colour" with value "black"
laptop_dictionary['year'] = 2018                                                # Adds a new key named "year" with value "2018"
laptop_dictionary['type'] = 'mini'                                              # Adds a new key named "mini" with value "mini"
print(laptop_dictionary)                                                        # Prints all keys and values of laptop_dictionary

# popitem() removes last entered item from a dictionary
print(laptop_dictionary.popitem())                                              # Prints recently removed item from laptop_dictionary