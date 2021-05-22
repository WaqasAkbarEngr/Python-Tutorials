def smallest_number():
    numbers = []
    entries = input("How many number you want to enter? ")
    entries = int(entries)
    while entries > 0:
        entered_number = input("Enter a number? ")
        numbers.append(entered_number)
        smallest_number = entered_number
        entries = entries - 1
    print()
    print("Your entered numbers are ",numbers)
    for x in numbers:
        if x < smallest_number:
            smallest_number = x
    print()
    print("Smallest number is",smallest_number)
    print()
    input("Press any key to exit")
    return ()
smallest_number()