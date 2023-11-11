class Solution(object):
    def isValid(self, nums):
        nums = [n for n in nums if n !='.']
        return len(set(nums)) == len(nums)
        

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValid(row):
                return False
        
        for col in zip(*board):
            if not self.isValid(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(block):
                    return False

        return True



        