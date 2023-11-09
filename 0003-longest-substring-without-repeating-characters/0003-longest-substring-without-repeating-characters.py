class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            curr = s[r]
            if curr in seen and seen[curr] >= l:
                l = seen[curr] + 1
            else:
                m = max(m, r- l + 1)
            seen[curr] = r
        return m 
