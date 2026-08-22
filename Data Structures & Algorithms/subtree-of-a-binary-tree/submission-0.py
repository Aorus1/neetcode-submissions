# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        elif root.left is None or root.right is None:
            if root.left is None and root.right is None:
                return False
            else: 
                if root.left is None:
                    return self.isSubtree(root.right, subRoot)
                else: 
                    return self.isSubtree(root.left, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q:
            if p.val != q.val:
                return False
        
            else:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True
                else:
                    return False
        else:
            return False


        