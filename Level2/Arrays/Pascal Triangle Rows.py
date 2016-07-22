# Given numRows, generate the first numRows of Pascal’s triangle.
#
# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
# Example:
#
# Given numRows = 5,
#
# Return
#
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]


class Solution:

    @staticmethod
    def get_row(a):
        res = []
        for line in range(1, a+1):
            c = 1
            row = []
            for i in range(1, line+1):
                row.append(c)
                c = int(c * (line - i)/i)
            res.append(row)
        return res

a1 = 3
res1 = Solution.get_row(a1)
print(res1, end=" ")
