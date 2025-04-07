#Problem 230

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0 # Counter for visited nodes

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = self.helper(root, k)
        return result.val if result else 0 # Return value or 0 if not found

    def helper(self, node: TreeNode, k: int) -> TreeNode:
        if not node:
            return None
        
        # Traverse left subtree
        left = self.helper(node.left, k)
        if left:
            return left # If found in left subtree
        
        self.count += 1 # Increment count for current node
        if self.count == k:
            return node # Found k-th smallest
        
        # Traverse right subtree
        return self.helper(node.right, k)