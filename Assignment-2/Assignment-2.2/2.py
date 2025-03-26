# 268. Missing numbers
nums.sort()

for i, v in enumerate(nums):
    if (i != v):
        return v-1
    if v == len(nums)-1:
        return v+1