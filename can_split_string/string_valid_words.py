valid_words = ["apple", "banana", "cherry", "dog", "cat"]
input_string = "applebanana"

def can_split_string(input_string, valid_words):
    if not input_string:
        return True

    for word in valid_words:
        if input_string.startswith(word):
            remaining = input_string[len(word):]
            if can_split_string(remaining, valid_words):
                return True

    return False

result = can_split_string(input_string, valid_words)
print(result)  # This should print True























# valid_words = ["apple", "banana", "cherry", "dog", "cat"]
# input_string = "applebananacherrydogcat"
#
# to_check = [input_string]
# print(to_check)
# while to_check:
#     current = to_check.pop()
#     for word in valid_words:
#         if current.startswith(word):
#             remaining = current[len(word):]
#             if remaining == "":
#                 print("Valid sequence found")
#                 exit()
#             to_check.append(remaining)
#
# print("No valid sequence found")
#
#

