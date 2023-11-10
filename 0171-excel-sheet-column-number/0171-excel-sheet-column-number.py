class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        alphabet = string.ascii_uppercase
        num = 0
        for char in columnTitle:
            num *= 26
            num += alphabet.find(char) + 1
        return num


        