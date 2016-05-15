# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
#  Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# Example :
# Given array S = {1 0 -1 0 -2 2}, and target = 0
# A solution set is:
#
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#     (-1,  0, 0, 1)
# Also make sure that the solution set is lexicographically sorted.
# Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR
# (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])


class Solution:

  @staticmethod
  def solution(a, target):
        hash = {}
        a.sort()
        result = []
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                k = j + 1
                l = len(a) - 1
                while k < l:
                    sum = a[i] + a[j] + a[k] + a[l]
                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    elif sum == target:
                        res = (a[i], a[j], a[k], a[l])
                        if res not in hash:
                            hash[res] = 1
                            result.append(res)
                        k += 1
                        l -= 1
        return result
number = [1, 0, -1, 0, -2, 2]
res1 = Solution.solution(number, 0)
print(res1)


