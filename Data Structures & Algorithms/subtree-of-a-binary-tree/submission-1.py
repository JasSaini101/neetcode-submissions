# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToList(self, root: Optional[TreeNode]):

        if not root:
            return [0]
        
        return([root.val] + self.treeToList(root.right) + self.treeToList(root.left))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        elif not root:
            return False

        if(root.val != subRoot.val):
            return(self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))
        
        if(self.treeToList(root) == self.treeToList(subRoot)):
            return(True)
        if(not self.treeToList(root) == self.treeToList(subRoot) and not root.right and not root.left):
            return(False)
        else:
            return(self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))

        