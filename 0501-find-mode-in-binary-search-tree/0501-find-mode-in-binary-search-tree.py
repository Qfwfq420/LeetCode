# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.map = {}

    def count(self, root):
        if not root:
            return None
        self.count(root.left)
        self.count(root.right)
        self.map[root.val] = self.map.get(root.val, 0) + 1


    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result =[]
        self.count(root)
        maxi = 0
        for x in self.map.values():
            maxi = max(maxi, x)
        for key, value in self.map.items():
            if value == maxi:
                result.append(key)
        return result

        