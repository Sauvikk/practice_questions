# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#
# The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
#
# The input corresponding to the above configuration :
#
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.
#
#  Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:

  @staticmethod
  def solution(s):
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if s[i][j] in row_set and s[i][j] != '.':
                    print('1')
                    return 0
                if s[j][i] in col_set and s[j][i] != '.':
                    print('2')
                    return 0
                row_set.add(s[i][j])
                col_set.add(s[j][i])

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                box_set = set()
                for i in range(x, x+3):
                    for j in range(y, y + 3):
                        if s[i][j] in box_set and s[i][j] != '.':
                            print('3')
                            return 0
                        box_set.add(s[i][j])
        return 1
sudoku = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5",
          "....8..79"]
res1 = Solution.solution(sudoku)
print(res1)


