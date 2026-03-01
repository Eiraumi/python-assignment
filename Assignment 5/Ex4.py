import re

def hide_phone_numbers(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    return re.sub(pattern, "[REDACTED]", text)


# Test thử
if __name__ == "__main__":
    text = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321;"
    print(hide_phone_numbers(text))