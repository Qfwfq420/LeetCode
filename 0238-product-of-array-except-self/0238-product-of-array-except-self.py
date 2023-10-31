class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answers = [1] * len(nums)
        for i in range(1, len(nums)):
            answers[i] = answers[i-1] * nums[i-1]
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answers[i] *= right
            right *= nums[i]
        return answers

        