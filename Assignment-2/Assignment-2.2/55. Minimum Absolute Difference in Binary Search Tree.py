#Problem 530

class Solution:
    def values(self,root):
        lst=[]
        if root is None:
            return
        else:
            lst.append(root.val)
            if root.left is not None:
                lst+=self.values(root.left)
            if root.right is not None:
                lst+=self.values(root.right)
        return lst

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst=list(self.values(root))
        lst.sort()
        mindiff=float('inf')
        for i in range(len(lst)-1):
            mindiff=min(mindiff,abs(lst[i]-lst[i+1]))
        return mindiff     