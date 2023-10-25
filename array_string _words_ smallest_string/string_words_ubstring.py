import itertools

def shortest_superstring(words):
    # Define a function to calculate the overlap between two words
    def overlap(a, b):
        max_len = min(len(a), len(b))
        for i in range(max_len, 0, -1):
            if a.endswith(b[:i]):
                return i
        return 0

    # Generate all permutations of the input words
    permutations = list(itertools.permutations(words))

    shortest = float('inf')
    shortest_superstring = ""

    # Iterate through each permutation to find the shortest superstring
    for perm in permutations:
        superstring = perm[0]
        for i in range(1, len(perm)):
            o = overlap(perm[i - 1], perm[i])
            superstring += perm[i][o:]

        if len(superstring) < shortest:
            shortest = len(superstring)
            shortest_superstring = superstring

    return shortest_superstring

# Example 2:
# input_words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
# input_words = ["alex","loves","leetcode"]
input_words = ["tef","efd", "ift","fdn","dnete"]


result = shortest_superstring(input_words)
print("Example Output:", result)
