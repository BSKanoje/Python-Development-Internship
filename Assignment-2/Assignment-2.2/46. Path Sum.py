#Problem 112

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # Subtract current node's value from targetSum
        targetSum -= root.val
        
        # Check if it's a leaf node and targetSum becomes zero
        if not root.left and not root.right:
            return targetSum == 0
        
        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)