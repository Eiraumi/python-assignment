def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# MAIN PROGRAM (test)
nums = [1, 2, 3, 4, 5]
result = sum_list(nums)
print(result)
