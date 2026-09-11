# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToList(self, root: Optional[TreeNode]):
        if not root:
            return '0'
        return(str(root.val) + self.treeToList(root.right) + self.treeToList(root.left))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        bigTree = self.treeToList(root)
        little = self.treeToList(subRoot)

        return(little in bigTree)

        