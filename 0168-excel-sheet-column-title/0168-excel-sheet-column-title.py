class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        alphabet = string.ascii_uppercase
        result = ''
        while columnNumber > 0:
            if columnNumber % 26 == 0:
                result += alphabet[-1]
                columnNumber -= 1
            else:
                result += alphabet[columnNumber % 26 - 1]
            columnNumber //= 26
        return result[::-1] 
