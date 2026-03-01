import re

def is_valid_course_code(code):
    pattern = r'^[A-Z]{2,3}[0-9]{3}$'
    return bool(re.match(pattern, code))


# Test thử cái đúng xem đc ko
if __name__ == "__main__":
    test_cases = ["TEC001", "AU006", "te001", "AB1234", "A123", "AB12"]

    for code in test_cases:
        print(code, "->", is_valid_course_code(code))