numbers = []

while True:
    s = input("Enter a number (press Enter to quit): ")
    if s == "":
        break
    numbers.append(float(s))

print("Smallest:", min(numbers))
print("Largest:", max(numbers))
