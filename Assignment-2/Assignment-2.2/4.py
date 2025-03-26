# 1. Two sum
def twoSum (nums, target):
    hashMap={}
    for index, val in enumerate(nums):
        diff = target-val

        if diff in hashMap:
            return [index, hashMap[diff]]
        hashMap[val] = index
        