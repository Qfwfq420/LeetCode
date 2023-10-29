class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = len(a) - 1
        y = len(b) - 1
        d = 0
        result = ''
        while x >= 0 or y >= 0 or d:
            total = d
            if x >= 0 :
                total += int(a[x])
                x -=1
            if y >= 0:
                total += int(b[y])
                y -=1
            d = total // 2
            result = str(total % 2) + result
        return result

        