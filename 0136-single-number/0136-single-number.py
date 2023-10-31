class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if not(nums[i] in nums[:i] or nums[i] in nums[i + 1:]):
                return nums[i]

        