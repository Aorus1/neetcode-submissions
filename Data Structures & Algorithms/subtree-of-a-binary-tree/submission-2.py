# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if node is None:
                return "#"
            return f"^{node.val},{serialize(node.left)},{serialize(node.right)}"
        s = serialize(root)
        t = serialize(subRoot)
        return self.kmp_search(t, s)

    def kmp_search(self, pattern, text):
        if not pattern:
            return True
        # Build failure function for pattern
        lps = [0] * len(pattern)
        k = 0
        for i in range(1, len(pattern)):
            while k > 0 and pattern[k] != pattern[i]:
                k = lps[k-1]
            if pattern[k] == pattern[i]:
                k += 1
            lps[i] = k
        
        # Search
        j = 0
        for i in range(len(text)):
            while j > 0 and pattern[j] != text[i]:
                j = lps[j-1]
            if pattern[j] == text[i]:
                j += 1
            if j == len(pattern):
                return True
        return False