# Find if Given number is power of 2 or not.
# More specifically, find if given number can be expressed as 2^k where k >= 1.
#
# Input:
#
# number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
# Output:
#
# return 1 if the number if a power of 2 else return 0
#
# Example:
#
# Input : 128
# Output : 1


class Solution:

  @staticmethod
  def solution(num):
        # <= 1 because 1 has a set bit but cannot be in the form of 2^k, k >= 1
        if num <= 1:
            return 0
        else:
            return not (num & (num-1))

num = 2 ** 68
print(num)
res = Solution.solution(num)
print(res)
