#Problem 700

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while True:
            if node is not None and node.val == val:
                return node
            elif node is not None and node.val>val:
                node = node.left
            elif node is not None and node.val<val:
                node = node.right
            else:
                return None
