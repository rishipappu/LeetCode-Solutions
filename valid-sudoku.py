class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.checkList(row):
                return False

        columnBoard = self.grabColumn(board)
        for row in columnBoard:
            if self.checkList(row):
                return False
        squareBoard = self.grab3x3(board)
        for row in squareBoard:
            if self.checkList(row):
                return False
        return True

    def checkList(self, nums: List[str]) -> bool:
        nums = [num for num in nums if num != "."]
        return len(nums) != len(set(nums))

    def grabColumn(self, board: List[List[str]]) -> List[List[str]]:
        newBoard = []
        row = 0
        column = 0
        while column < 9:
            newColumn = []
            while row < 9:
                newColumn.append(board[row][column])
                row += 1
            newBoard.append(newColumn)
            row = 0
            column += 1
        return newBoard

    def grab3x3(self, board: List[List[str]]) -> List[List[str]]:
        squares = []
        for i in range(3):
            for j in range(3):
                square = []
                for x in range(3 * i, 3 * i + 3):
                    for y in range(3 * j, 3 * j + 3):
                        square.append(board[x][y])
                squares.append(square)
        return squares
