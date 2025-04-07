#Problem 108

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.buildBST(nums, 0, len(nums) - 1)

    def buildBST(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        mid = (start + end) // 2 # Calculate middle index
        root = TreeNode(nums[mid])

        root.left = self.buildBST(nums, start, mid - 1)
        root.right = self.buildBST(nums, mid + 1, end)

        return root