def check_leap_year():
    """
    Asks the user to enter a year and checks whether it is a leap year.
    """

    year = int(input("Enter a year: "))

    if year % 400 == 0:
        print("The year is a leap year.")
    elif year % 100 == 0:
        print("The year is not a leap year.")
    elif year % 4 == 0:
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")


# Call the function
check_leap_year()
