class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        connections = collections.defaultdict(set)
        for i, j in adjacentPairs:
            connections[i].add(j)
            connections[j].add(i)
        for node, vec in connections.items():
            if len(vec) == 1:
                break
        result = [node]
        while connections[node]:
            new = connections[node].pop()
            result.append(new)
            connections[new].remove(node)
            node = new
        return result
