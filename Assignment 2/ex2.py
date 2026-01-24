def describe_cabin():
    """
    Asks the user to enter the cabin class of a cruise ship
    and prints a description based on the cabin class.
    """

    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()

    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Cabin above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


# Call the function
describe_cabin()
