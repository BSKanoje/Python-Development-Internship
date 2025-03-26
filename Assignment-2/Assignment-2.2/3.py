# 448. Find all numbers disappeared in an array
set_nums = set(nums)
ret = []
for i in range(l, len(nums)+1):

    if i not in set_nums:
        ret.append(i)

return ret