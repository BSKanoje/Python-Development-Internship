#Problem 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.treeHeight(root)

    def treeHeight(self, node: TreeNode) -> int:
        if not node:
            return 0 

        left_height = self.treeHeight(node.left) 
        right_height = self.treeHeight(node.right)

        return 1 + max(left_height, right_height) 