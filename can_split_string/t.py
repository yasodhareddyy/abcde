def can_split_string(input_string, valid_words):
    words_used = set()

    for word in input_string.split():
        if word in valid_words and word not in words_used:
            words_used.add(word)
        else:
            return False

    return True

# Example usage:
valid_words = ["apple", "banana", "cherry", "dog", "cat"]
input_string = "apple banana cherry dog cat"
result = can_split_string(input_string, valid_words)
print(result)  # This should print True
