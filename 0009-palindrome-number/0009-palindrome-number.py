class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = [i for i in str(x)]
        return y[:len(y)//2] == y[:(len(y) - 1)//2:-1]

        