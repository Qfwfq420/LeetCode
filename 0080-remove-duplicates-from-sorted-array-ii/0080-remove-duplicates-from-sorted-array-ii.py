class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)
        