# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The cell itself does not count as an adjacent cell.
# The same letter cell may be used more than once.
#
# Example :
#
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# word = "ABCCED", -> returns 1,
# word = "SEE", -> returns 1,
# word = "ABCB", -> returns 1,
# word = "ABFSAB" -> returns 1
# word = "ABCD" -> returns 0
# Note that 1 corresponds to true, and 0 corresponds to false.


class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0) == 1:
                    result = 1
        return result

    def dfs(self, board, word, i, j, k):
        m = len(board)
        n = len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        if board[i][j] == word[k]:
            temp = board[i][j]
            if k == len(word) - 1:
                return 1
            elif (self.dfs(board, word, i - 1, j, k + 1)
                  or self.dfs(board, word, i + 1, j, k + 1)
                  or self.dfs(board, word, i, j - 1, k + 1)
                  or self.dfs(board, word, i, j + 1, k + 1)):
                return 1
        return 0


b = [ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ]
print(Solution().exist(b, "BCDCB"))
