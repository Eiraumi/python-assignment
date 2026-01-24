import math

def calculate_unit_price(diameter_cm, price):
    """
    Calculates and returns the unit price of a pizza per square meter.
    """

    radius_m = (diameter_cm / 2) / 100      # đổi cm → m
    area = math.pi * radius_m ** 2          # diện tích hình tròn (m²)
    unit_price = price / area               # giá trên mỗi m²

    return unit_price


def main():
    # Pizza 1
    d1 = float(input("Enter the diameter of pizza 1 (cm): "))
    p1 = float(input("Enter the price of pizza 1 (USD): "))

    # Pizza 2
    d2 = float(input("Enter the diameter of pizza 2 (cm): "))
    p2 = float(input("Enter the price of pizza 2 (USD): "))

    unit_price_1 = calculate_unit_price(d1, p1)
    unit_price_2 = calculate_unit_price(d2, p2)

    print(f"Pizza 1 unit price: {unit_price_1:.2f} USD/m²")
    print(f"Pizza 2 unit price: {unit_price_2:.2f} USD/m²")

    if unit_price_1 < unit_price_2:
        print("Pizza 1 provides better value for money.")
    elif unit_price_2 < unit_price_1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


# Run the main program
main()
