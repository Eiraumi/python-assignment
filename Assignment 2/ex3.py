def check_hemoglobin():
    """
    Asks the user for biological sex and hemoglobin value (g/l).
    Notifies whether the hemoglobin value is low, normal, or high.
    """

    sex = input("Enter biological sex (male/female): ").strip().lower()
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hemoglobin < 117:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    elif sex == "male":
        if hemoglobin < 134:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 167:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    else:
        print("Invalid biological sex")


# Call the function
check_hemoglobin()
