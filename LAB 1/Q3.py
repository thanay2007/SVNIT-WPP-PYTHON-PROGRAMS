while True:
    print("To convert feet to inches enter 1")
    print("To convert feet to yard enter 2")
    print("To convert feet to miles enter 3")
    print("To convert feet to millimeters enter 4")
    print("To convert feet to centimeters enter 5")
    print("To convert feet to meters enter 6")
    print("To convert feet to kilometers enter 7")

    ch = int(input("Enter a number to choose the option: "))
    feet = float(input("Enter the measurement in feet: "))

    conversions = [["Inches: ", feet * 12],["Yard: ", feet * 0.33],["Miles: ", feet * 0.000189394],
                   ["Millimeter: ", feet * 304.8],["Centimeters: ", feet * 30.48],
                   ["Meters: ", feet * 0.3048],["Kilometers: ", feet * 0.0003048]]

    for i in range(2):
        print(conversions[ch - 1][i], end='')

    a = input("\nDo you want to continue? (y/n): ").lower()

    if a == 'n':
        print("Thank you")
        break
    elif a != 'y':
        print("Invalid input")
        break
