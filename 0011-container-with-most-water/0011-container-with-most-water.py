class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max = min(height[0], height[-1]) * (len(height) -1)
        while l < r:
            if min(height[l], height[r]) * (r - l) > max:
                max = min(height[l], height[r]) * (r - l)
            if min(height[l], height[r]) == height[l]:
                l += 1
            else:
                r -= 1
        return max
