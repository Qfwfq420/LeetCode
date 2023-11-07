class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(x for x in s if x.isalpha() or x.isnumeric()).lower()
        return s[:len(s)//2] == s[(len(s) + 1)//2:][::-1]

        