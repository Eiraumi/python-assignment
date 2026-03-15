def remove_odds(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result


nums = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_odds(nums)

print("Original list:", nums)
print("List without odd numbers:", new_list)