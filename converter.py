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
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Liters to Gallons")
    print("4. Gallons to Liters")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
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


def convert():
    match choice:
        case 1:
            print(f"{chosen_number} to Celsius is {(chosen_number - 32) * 5/9:.2f}")
        case 2:
            print(f"{chosen_number} to Fahrenheit is {(chosen_number * 9/5) + 32:.2f}")
        case 3:
            print(f"{chosen_number} to Gallons is {0.264172 * chosen_number:.2f}")
        case 4:
            print(f"{chosen_number} to Liters is {3.785 * chosen_number:.2f}")
        case 5:
            print(f"{chosen_number} to Pounds is {2.20462 * chosen_number:.2f}")
        case 6:
            print(f"{chosen_number} to Kilograms is {0.453592 * chosen_number:.2f}")


convert()
