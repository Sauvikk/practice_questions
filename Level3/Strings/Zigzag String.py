# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
# **Example 2 : **
# ABCD, 2 can be written as
#
# A....C
# ...B....D
# and hence the answer would be ACBD.
# http://www.geeksforgeeks.org/print-concatenation-of-zig-zag-string-form-in-n-rows/

import itertools


class Solution:

  @staticmethod
  def solution(s, n):
            if n == 1:
                return s
            result = [[] for y in range(n)]
            row = 0
            down = True
            for i in range(len(s)):
                result[row].append(s[i])
                if row == n - 1:
                    down = False
                elif row == 0:
                    down = True
                row = row + 1 if down else row - 1
            return ''.join(list(itertools.chain(*result)))

s = "PAYPALISHIRING"
res = Solution.solution(s, 3)
print(res)
