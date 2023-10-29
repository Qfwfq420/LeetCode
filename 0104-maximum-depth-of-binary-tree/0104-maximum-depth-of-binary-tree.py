# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth(self, root, d):
        if not root:
            return d
        else:
            d += 1
            return max(self.depth(root.left, d), self.depth(root.right, d))


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = 0 
        return self.depth(root, d)
        