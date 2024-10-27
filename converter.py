print("What do you want to convert from?\n")

while True:
    try:
        chosen_number = float(input("Enter the number you want to convert: "))
    except ValueError:
        print("Make sure your choice is a number. \n")
        continue
    else:
        break
while True:
    print("1. to Celsius")
    print("2. to Fahrenheit")
    print("3. to Gallons")
    print("4. to Liters")
    print("5. to Pounds")
    print("6. to Kilograms")
    try:
        choice = int(input("Choose what you want to convert to: "))
    except ValueError:
        print("Make sure your choice is a number. \n")
        continue
    else:
        if choice > 6 or choice == 0:
            print("Make sure your number is between 1 and 7.\n")
            continue
        else:
            break
