class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(node):

            
            if not node:
                return False

            
            if k - node.val in seen:
                return True

            
            seen.add(node.val)

            
            leftSide = helper(node.left)
            rightSide = helper(node.right)

            
            return leftSide or rightSide

        seen = set()        

        return helper(root)