def word_frequency(text):
    words = text.split()
    total_words = len(words)

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top5 = dict(sorted_words[:5])

    top5_count = sum(top5.values())

    proportion = (top5_count / total_words) * 100

    print("Top 5:", top5)
    print("Total number of words:", total_words)
    print("Proportion of 5 most common words:", round(proportion, 2), "%")


text = input("Enter a text: ")

word_frequency(text)