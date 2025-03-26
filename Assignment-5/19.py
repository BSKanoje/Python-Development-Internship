# Write a Python program to find smallest and largest word in a given string.

def find_smallest_and_largest_word(s):
    words = s.split()

    if not words:
        return None, None

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)

    return smallest_word, largest_word

input_string = "Write a Python program to find smallest and largest word"
smallest, largest = find_smallest_and_largest_word(input_string)

print(f"Input string: {input_string}")
print(f"Smallest word: {smallest}")
print(f"Largest word: {largest}")
