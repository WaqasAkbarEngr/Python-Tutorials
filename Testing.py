entry = input("Enter a positive number greater than 1 ? ")
entry = int(entry)
half = entry //2

if entry < 2 and entry != 1:
    print("-------------------------------")
    print("|                             |")
    print("|  You entered wrong number   |")
    print("|                             |")
    print("-------------------------------")
elif entry == 1:
    print("-------------------------------")
    print("|                             |")
    print("|   1 is not a prime number   |")
    print("|                             |")
    print("-------------------------------")
else:
    for x in range(2,half):
        if entry % 2 == 0:
            print("-------------------------------")
            print("|                             |")
            print("| Entered number is not prime |")
            print("|                             |")
            print("-------------------------------")
            break
    else:
            print("----------------------------")
            print("|                          |")
            print("| Entered number is  prime |")
            print("|                          |")
            print("----------------------------")

input("Press any key to exit")