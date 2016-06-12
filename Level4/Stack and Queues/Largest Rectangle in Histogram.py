# Given n non-negative integers representing the histogram’s bar height
# where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
# Example Histogram
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# Example2
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.


class Solution:

  @staticmethod
  def solution(hist):
        if not hist or len(hist) == 0:
            return 0
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

        while len(stack) != 0:
            print(stack)
            print(i)
            index = stack.pop()
            height = hist[index]
            width = i if len(stack) == 0 else i - stack[-1] - 1
            max_area = max(height*width, max_area)
        return max_area


arr = [2, 1, 5, 6, 2, 3]
res = Solution.solution(arr)
print(res)
