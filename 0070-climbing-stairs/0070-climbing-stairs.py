class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        return self.fib(n, memo)


    def fib(self, n, memo):
        if n < 3:
            return n
        if n not in memo:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]