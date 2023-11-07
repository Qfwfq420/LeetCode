class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        trip, curr, start = 0, 0, 0
        for i in range(len(gas)):
            trip += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        if trip >= 0:
            return start
        return -1

