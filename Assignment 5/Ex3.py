import re

def sum_numbers_in_text(text):
    numbers = re.findall(r'[0-9]+', text)
    total = 0
    for num in numbers:
        total += int(num)
    return total


if __name__ == "__main__":
    text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
    print(sum_numbers_in_text(text))