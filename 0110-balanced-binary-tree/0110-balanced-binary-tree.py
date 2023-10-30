# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        left, right = self.depth(root.left) , self.depth(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1 



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) >= 0
        