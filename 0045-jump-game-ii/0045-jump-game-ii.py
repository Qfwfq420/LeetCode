class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        n = len(nums) - 1
        m = min(n, max(nums))
        while n != 0:
            for i in range(m, 0, -1):
                if nums[n-i] + n - i >= n:
                    n = n-i
                    jumps += 1
                    m = min(n, max(nums))
                    break
        return jumps

