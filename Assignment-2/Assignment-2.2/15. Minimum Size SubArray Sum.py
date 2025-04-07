class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, s, m = 0, 0, float('inf')
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                m = min(m, r - l + 1)
                s -= nums[l]
                l += 1
        return 0 if m == float('inf') else m