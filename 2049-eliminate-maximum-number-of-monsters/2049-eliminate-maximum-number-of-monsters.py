class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        priority = [-(dist[i] // -speed[i]) for i in range(len(dist))]
        priority.sort()
        monster = 0
        for i in range(len(dist)):
            if priority[i] <= i:
                break
            monster += 1
        return max(1, monster)
        