class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        while t:
            if len(s) == 0:
                return True
            if s[0] == t[0]:
                s = s[1:]
            t = t[1:]
        return len(s) == 0

