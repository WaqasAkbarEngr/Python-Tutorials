# While writing a string a single quotation marks or double quotation marks are used
# For example

print ( "This is a string which is written between double quotation marks" )
# Or
print ( 'This string is written between single quotation marks' )

# In order to find the length of a string in python "len()" is used
# For example

string = 'This is a string in python program          '
length = len(string)
print( "The length of the string is" , length )     #print statement in this line printing multiple line in
                                                    # one line on screen

# In order to make all the letter lowercase in a string, "variable_name.lower()" is used
# In order to make all the letter uppercase in a string, "variable_name.upper()" is used
# For example

lowercase = string.lower()      # In this line string.lower() is coverting all the letter in the string to lowercase
                                # and storing them in variable named lowercase
uppercase = string.upper()      # In this line string.upper() is coverting all the letter in the string to lowercase
                                # and storing them in variable named uppercase
print(lowercase + ' written in lowercase')
# In above line, print statement is printing lowercase letters stored in variable name lowercase
print(uppercase + " written in uppercase")
# In above line, print statement is printing uppercase letters stored in variable name uppercase

# In order to replace a part of string, "variable_name.replace("being replaced","replacing string")" is used
# For example

print(string.replace("This","That"))  # In this line, word This in variable named string is replaced by That

# variable_name.split() is used to split string whenever character given in paranthesis comes
# For example

print(string.split("a"))    # split() checks the string and whenever character a comes it split the string at that point

# variable_name.strip() removes all the spaces that comes at the end of the string
# For example

print(string.strip(),string)    # In this line strip() is eliminating all the spaces at the end of the string that is
                                # stored in the variable named string

# variable_name[a:b] or variable_name[n] is used to get string in range from a to b or nth character in a string
# For example

print("The first five entries in variable string are (" , string[0:5] , ")" )
# In above line string[0:5] is fetching only first 6 characters from the string