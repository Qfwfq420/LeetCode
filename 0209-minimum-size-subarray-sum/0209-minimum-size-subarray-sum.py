class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum, i, j = 0, 0, 0
        m = float('inf')
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                sum -= nums[i]
                m = min(m, j-i+1)
                i +=1 
            j += 1
        if m == float('inf'):
            return 0
        return m 
                
        