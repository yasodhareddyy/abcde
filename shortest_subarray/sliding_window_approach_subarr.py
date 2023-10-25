def find_shortest_subarray(text, word_list):
    words = set(word_list)
    min_len = float('inf')
    start, end = 0, 0
    left = 0
    words_count = {word: 0 for word in word_list}

    for right, word in enumerate(text):
        if word in words:
            words_count[word] += 1

        while all(words_count[word] > 0 for word in words):
            if right - left < min_len:
                min_len = right - left
                start, end = left, right

            left_word = text[left]
            if left_word in words:
                words_count[left_word] -= 1
            left += 1

    return (start, end) if min_len != float('inf') else "No subarray found"

# Read text data from a file
with open("text_data.txt", "r") as file:
    text_document = file.read().split()

word_list = ["Python", "program", "subarray"]

result = find_shortest_subarray(text_document, word_list)
if isinstance(result, tuple):
    start, end = result
    print(f"Shortest subarray containing all words: {' '.join(text_document[start:end+1])}")
    print(f"Start index: {start}, End index: {end}")
else:
    print(result)

