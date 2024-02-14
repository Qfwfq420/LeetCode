class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            j = 0
            while i + j < len(s) and s[i] == s[i + j]:
                j += 1
            i += j 
            count += (j + 1) * j / 2 
        return count % (pow(10, 9) + 7)
        