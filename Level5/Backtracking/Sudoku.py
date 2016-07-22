# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'
# You may assume that there will be only one unique solution.
#
# Example :
#
# [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
#
# and we would expect your program to modify the above array of array of characters to
#
# [[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]


import itertools

class Solution:

  def is_valid(self, board, i, j, c):

        for row in range(9):
            if board[row][j] == c:
                return False

        for col in range(9):
            if board[i][col] == c:
                return False

        for row in range(3*int(i/3), 3*int(i/3+1)):
            for col in range(3*int(j/3), 3*int(j/3+1)):
                if board[row][col] == c:
                    return False

        return True

  def generate(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for num in range(1, 9+1):
                        if self.is_valid(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.generate(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

  def solution(self, board):
        for i in range(len(board)):
            board[i] = list(board[i])
        self.generate(board)
        for i in range(len(board)):
            board[i] = ''.join(itertools.chain(board[i]))
        return board

res1 = Solution().solution([ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ])
print(res1)
