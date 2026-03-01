import re

def is_valid_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))


# Test thử
if __name__ == "__main__":
    test_cases = [
        "#FFFFFF",
        "#ff0000",
        "#1A2b3C",
        "123456",
        "#FFF",
        "#GGGGGG",
        "#1234567"
    ]

    for color in test_cases:
        print(color, "->", is_valid_hex_color(color))