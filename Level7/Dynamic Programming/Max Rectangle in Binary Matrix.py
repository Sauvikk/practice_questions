# Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.
#
# Bonus if you can solve it in O(n^2) or less.
#
# Example :
#
# A : [  1 1 1
#        0 1 1
#        1 0 0
#     ]
#
# Output : 4
#
# As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
# http://stackoverflow.com/questions/3806520/finding-maximum-size-sub-matrix-of-all-1s-in-a-matrix-having-1s-and-0s
# http://www.programcreek.com/2014/05/leetcode-maximal-rectangle-java/


class Solution:
    # @param A : list of list of integers
    # @return an integer

    def max_area(self, hist):
        stack = []
        max_area = 0
        i = 0
        while i < len(hist):
            if len(stack) == 0 or hist[i] >= hist[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                height = hist[index]
                width = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(height*width, max_area)
        return max_area

    def maximalRectangle(self, matrix):
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])
        height = [[0 for x in range(n+1)]for x in range(m)]
        maximum_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    height[i][j] == 0
                else:
                    height[i][j] = 1 if i == 0 else height[i-1][j] + 1
        for i in range(m):
            area = self.max_area(height[i])
            maximum_area = max(maximum_area, area)
        return maximum_area


# mat = [
#   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
#   [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
#   [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
#   [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
# ]
mat = [[1]]
print(Solution().maximalRectangle(mat))
