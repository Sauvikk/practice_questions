# http://www.geeksforgeeks.org/rearrange-given-array-place/
class Solution:

  @staticmethod
  def solution(arr):
        n = len(arr)
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        for i in range(n):
            arr[i] = int(arr[i]/n)
        return arr

arr = [1, 0]
res = Solution.solution(arr)
print(res)

