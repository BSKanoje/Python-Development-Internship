# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4

class PairFinder:
    def find_pair(self, numbers, target):
        num_to_index = {}
        for i, num in enumerate(numbers):
            if target - num in num_to_index:
                return (num_to_index[target - num], i)
            num_to_index[num] = i
        return None

finder = PairFinder()
print(finder.find_pair([90, 20, 10, 40, 50, 60, 70], 50))
