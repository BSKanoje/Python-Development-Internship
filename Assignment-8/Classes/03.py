# Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]].

class SubsetGenerator:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

generator = SubsetGenerator()
print(generator.subsets([4, 5, 6]))
