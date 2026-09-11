# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        curr = root
        lower = min(p.val,q.val)
        greater = max(p.val,q.val)

        if curr.val <= greater and curr.val >= lower:
            return curr

        if curr.val < greater:
            curr = curr.right
        else:
            curr = curr.left

        return self.lowestCommonAncestor(curr, p, q) 