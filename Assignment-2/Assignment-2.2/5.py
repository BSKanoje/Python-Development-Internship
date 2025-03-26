#  1365. How many numbers are smaller than the current number
temp =sorted((nums))
d={}

for i, num in enumerate(temp):
    if num not in d:
        d[num] = i
ret=[]

for i in nums:
    ret.append(d[i])

return ret