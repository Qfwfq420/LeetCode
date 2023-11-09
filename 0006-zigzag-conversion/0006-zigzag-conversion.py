class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        out = ['' for i in range(numRows)]
        x = 0
        flag = True
        for i in range(len(s)):
            out[x] += s[i]         
            if flag:
                x = (x+1)%numRows
            else:
                x -=1
            if x % numRows == numRows - 1 or x % numRows == 0:
                flag = not flag
        return ''.join(out)