class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        priority = [-(dist[i] // -speed[i]) for i in range(len(dist))]
        priority.sort()
        for i in range(len(dist)):
            if priority[i] <= i:
                i -= 1
                break
        return i + 1
        