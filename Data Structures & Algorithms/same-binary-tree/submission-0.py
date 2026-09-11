# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToList(self, tree):
        if(tree == None):
            return ["null"]
        return([tree.val] + self.treeToList(tree.right) + self.treeToList(tree.left))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(self.treeToList(p) == self.treeToList(q)):
            return True
        return False
        