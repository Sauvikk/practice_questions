# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example :
#
# Input : [1 2 2 3 1]
# Output : 3


class Solution:

  @staticmethod
  def solution(arr):
        res = 0
        for num in arr:
            print(str(res) + ' XOR ' + str(num), end=' = ')
            res ^= num
            print(res)
        return res

arr = [1, 2, 2, 3, 1]
res = Solution.solution(arr)
print('ans')
print(res)
