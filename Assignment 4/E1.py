numbers = []

while True:
    s = input("Enter a number (press Enter to quit): ")
    if s == "":
        break
    numbers.append(int(s))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)

