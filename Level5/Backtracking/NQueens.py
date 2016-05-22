# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens’ placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution:

  def is_safe(self, board, row, col, n):
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row
        j = col
        while j >= 0 and i < n:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True

  def solve_util(self, board, col, n, result):
        if col >= n:
            return True
        for i in range(n):
            if self.is_safe(board, i, col, n):
                board[i][col] = 'Q'
                if col == n - 1:
                    result.append([''.join([str(c) for c in l]) for l in board])
                # for one solution
                # if self.solve_util(board, col+1, n, result):
                #         return True
                self.solve_util(board, col+1, n, result)
                board[i][col] = '.'
        return False

  def solution(self, n):
            board = [['.']*n for _ in range(n)]
            result = []
            self.solve_util(board, 0, n, result)
            return result


res1 = Solution().solution(0)
print(res1)
