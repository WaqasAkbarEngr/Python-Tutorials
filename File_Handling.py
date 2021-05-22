f = open("file.txt","w")
f.write("Wecome to file handling in python\n")
f.write("This is the second line")
x = 12
y = 15
z = x + y
z = str(z)
f.write("\nThe sum of two numbers is ")
f.write(z)