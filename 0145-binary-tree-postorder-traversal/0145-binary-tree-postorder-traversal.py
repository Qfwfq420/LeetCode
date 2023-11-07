# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorder(self, root, post):
        if not root:
            return 
        self.postorder(root.left, post)
        self.postorder(root.right, post)
        post.append(root.val)
        return post



          
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        post = []
        return self.postorder(root, post)

        