# Given N * M field of O's and X's, where O=white, X=black
# Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
#
# Example:
#
# OOOXOOO
# OOXXOXO
# OXOOOXO
#
# answer is 3 shapes are  :
# (i)    X
#      X X
# (ii)
#       X
#  (iii)
#       X
#       X
# Note that we are looking for connected shapes here.
#
# For example,
#
# XXX
# XXX
# XXX
# is just one single connected black shape.


class Solution:

    def dfs(self, arr, i, j, visit, r, c):
            if i < 0 or i > r - 1:
                return
            if j < 0 or j > c - 1:
                return
            if arr[i][j] == 'O' or visit[i][j]:
                return

            visit[i][j] = True
            self.dfs(arr, i + 1, j, visit, r, c)
            self.dfs(arr, i - 1, j, visit, r, c)
            self.dfs(arr, i, j + 1, visit, r, c)
            self.dfs(arr, i, j - 1, visit, r, c)

    def sol(self, A):
        r = len(A)
        c = len(A[0])
        count = 0
        visit = [[False for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if A[i][j] == 'X' and not visit[i][j]:
                    self.dfs(A, i, j, visit, r, c)
                    count += 1
        return count


x1 = ["OOOXOOO",
     "OOXXOXO",
     "OXOOOXO"]

x= ["XXX",
"XXX",
"XXX"]
print(Solution().sol(x1))
