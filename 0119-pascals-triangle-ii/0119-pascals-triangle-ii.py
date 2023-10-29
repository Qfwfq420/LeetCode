class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        if rowIndex == 0:
            return [1]
        for i in range((rowIndex + 2)//2 ):
            p = 1
            for j in range(i):
                p *= rowIndex - j
                p /= j + 1
            result.append(p)
        if rowIndex % 2 == 0:
            return result[:-1] + result[::-1]
        else:
            return result + result[::-1]

        