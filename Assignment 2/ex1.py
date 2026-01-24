def check_zander_size():
    """
    Asks the user for the length of a zander in centimeters.
    Checks whether the fish meets the minimum size limit (42 cm).
    If not, instructs the user to release the fish and tells
    how many centimeters it is below the size limit.
    """

    length = float(input("Enter the length of the zander in centimeters: "))
    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print("The zander does not meet the size limit.")
        print("Release the fish back into the lake.")
        print(f"The fish is {difference:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit. You can keep the fish.")


# Call the function
check_zander_size()
