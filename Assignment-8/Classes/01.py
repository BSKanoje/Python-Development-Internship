# Write a python class to convert an integer into a roman numeral and viceversa

class RomanConverter:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        self.roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def int_to_roman(self, num):
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // self.val[i]):
                roman_num += self.syb[i]
                num -= self.val[i]
            i += 1
        return roman_num

    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_to_int[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

converter = RomanConverter()
print(converter.int_to_roman(3549))
print(converter.roman_to_int("MMMDXLIX"))
