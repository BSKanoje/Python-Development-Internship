"""
A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

Examples
The following are examples of balanced delimiter strings:

()[]{}
([{}])
([]{})
The following are examples of invalid strings:
([)]
([]
[])
([})
Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

Input:
([{}])
Output:
True
"""

def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(bracket_map.values())
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    return not stack

input_string = "([{}])"
print(is_balanced(input_string))
