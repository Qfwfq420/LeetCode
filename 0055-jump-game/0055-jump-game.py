class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max = 0 
        for i in range(len(nums)):
            if max < i:
                return False
            if nums[i] + i > max:
                max = nums[i] + i 
        return True
        