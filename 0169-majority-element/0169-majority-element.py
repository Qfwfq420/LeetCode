class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in set(nums):
            if nums.count(x) >= (len(nums) + 1) // 2:
                return x 