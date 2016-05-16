class Solution:

  @staticmethod
  def solution(a):
        a_len = len(a)
        res = []
        for D in range(2 * a_len):
            row = []
            for i in range(D+1):
                if i < a_len and (D - i) < a_len:
                    row.append(a[i][D-i])
            if row:
                res.append(row)

        return res

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
res = Solution.solution(a)
print(res)
