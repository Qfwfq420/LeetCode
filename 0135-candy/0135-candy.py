class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for i in range(len(ratings))]
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i + 1]:
                candy[i + 1] = max(candy[i] + 1, candy[i+1])
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candy[i] = max(1+candy[i +1], candy[i])
        return sum(candy)
        