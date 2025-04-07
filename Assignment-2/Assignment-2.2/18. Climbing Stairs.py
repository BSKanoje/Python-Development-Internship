#Problem 70

class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        a1=1
        for i in range(2,n+1):
            curr=a+a1
            a=a1
            a1=curr
        return a1
        