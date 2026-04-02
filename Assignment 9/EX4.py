def caesar_cipher(file_name, shift, direction):
    result = ""

    if direction == "left":
        shift = -shift

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:

                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)

                elif char.islower():
                    result += chr((ord(char) - 97 + shift) % 26 + 97)

                else:
                    result += char

    with open("cipher.txt", 'w', encoding='utf-8') as file:
        file.write(result)

    return result


print(caesar_cipher("TEST.txt", 3, "right"))