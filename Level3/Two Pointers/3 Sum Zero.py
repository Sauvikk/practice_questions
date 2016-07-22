# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
#  Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
# For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# (-1, 0, 1)
# (-1, -1, 2)


class Solution:

  @staticmethod
  def solution(arr):
            arr.sort()
            min = 2**31 - 1
            res = []
            for i in range(len(arr)):
                j = i + 1
                k = len(arr) - 1
                while j < k:
                    sum = arr[i] + arr[j] + arr[k]
                    temp = []
                    if sum == 0:
                        temp.append(arr[i])
                        temp.append(arr[j])
                        temp.append(arr[k])
                        j += 1
                        k -= 1
                        if temp not in res:
                            res.append(temp)
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
            return res

arr = [-1, 0, 1, 2, -1, -4]
res = Solution.solution(arr)
print(res)
