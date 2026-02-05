def remove_uneven(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


# MAIN PROGRAM (test)
original = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = remove_uneven(original)

print("Original list:", original)
print("Even numbers only:", filtered)
