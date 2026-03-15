numbers = []

while True:
    user_input = input("Enter a number (press Enter to stop): ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

print("Five greatest numbers:")

for num in numbers[:5]:
    print(num)