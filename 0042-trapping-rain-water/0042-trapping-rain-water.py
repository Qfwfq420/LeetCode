class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        water, l, r, lmax, rmax = 0, 0, n - 1 , 0, 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    water += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    water += rmax - height[r]
                r -= 1
        return water 

            


