class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        if target > nums[h]:
            return h + 1
        while l <= h:
            m = (l + h) // 2
            if target == nums[m]:
                return m 
            elif target < nums[m]:
                h = m -1
            else:
                l = m + 1
        return l