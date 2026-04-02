def average_score(file_name):
    total = 0
    count = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() != "":
                name, score = line.strip().split(",")
                total += int(score)
                count += 1
    if count == 0:
        return 0
    return total / count
print(average_score("scores.txt"))