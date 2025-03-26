# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(words):
    return max(words, key=len)

words = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Rust', 'Go']
# words = [word.lower() for word in words]

print(longest_word(words))
