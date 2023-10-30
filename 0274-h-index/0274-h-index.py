class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i in range(len(citations), -1, -1):
            cite = [citations[j] >= i for j in range(len(citations))]
            if cite.count(True) >= i:
                return i
        return 0