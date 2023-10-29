class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        prof = 0
        for price in prices[1:]:
            prof = max(prof, price - buy)
            buy = min(buy, price)
        return prof
        