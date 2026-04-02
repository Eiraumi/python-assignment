def find_keyword_lines(file_name, keyword):
    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):  # đếm từ 1
            if keyword in line:
                result.append(i)
    return result
print(find_keyword_lines("TEST.txt", "Hiếu"))