# variable types are not needed to be declared in python
# only value of variable is assigned.
# python automatically detects type of entered data
# for example

numbers = 12345 # CAUTION! variable name is case sensitive

# In above statement variable named numbers is declared by giving it numeric value
# python will detect its type and automatically assign that type to it i.e. integer

python_version = 3.7

# In above statement variable named python_version is declared by giving it numeric value
# python will detect its type and automatically assign that type to it i.e. float

################################################################################################
# NOTE: One thing to be noted here is that if numeric value is in decimal form then it will be #
# assigned float type and if it is without decimal point the it will be assigned integer type  #
################################################################################################

complex = 123j

# In above statement variable named complex is declared by giving it numeric value along with character j
# python will detect its type and automatically assign that type to it i.e. complex

program = 'this is my first program'

# In above statement a variable named program is declared by just giving it string value
# python will detect its type and automatically assign that type to it i.e. string

print (type(numbers))
# This statement outputs the type of variable named numbers

print (type(python_version))
# This statement outputs the type of variable named python_version

print (type(program))
# This statement outputs the type of variable named program

print (type(complex))
# This statement outputs the type of variable named complex