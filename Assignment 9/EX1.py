def count_lines(file_name):
    count = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count

print(count_lines("TEST.txt"))