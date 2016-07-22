# Given an array of integers, every element appears thrice except for one which occurs once.
#
# Find that element which does not appear thrice.
#
# Note: Your algorithm should have a linear runtime complexity.
#
# Could you implement it without using extra memory?
#
# Example :
#
# Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Output : 4
# http://stackoverflow.com/questions/7338070/finding-an-element-in-an-array-where-every-element-is-repeated-odd-number-of-tim


class Solution:

  @staticmethod
  def solution(arr):
        ones = 0
        twos = 0
        for num in arr:
            twos |= ones & num
            ones ^= num
            not_threes = ~(ones & twos)
            ones &= not_threes
            twos &= not_threes
        return ones

arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
res = Solution.solution(arr)
print(res)
