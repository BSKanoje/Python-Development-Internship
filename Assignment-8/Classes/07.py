# Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello'

class StringReverser:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

reverser = StringReverser()
print(reverser.reverse_words('hello .py'))
