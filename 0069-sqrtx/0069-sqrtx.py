class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0 
        h  = x
        while l <= h:
            m = (l + h) // 2
            if m * m < x:
                l = m + 1
            elif m * m > x:
                h = m - 1
            else:
                return m 
        return h