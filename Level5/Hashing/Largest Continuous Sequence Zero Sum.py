# Find the largest continuous sequence in a array which sums to zero.
#
# Example:
#
#
# Input:  {1 ,2 ,-2 ,4 ,-4}
# Output: {2 ,-2 ,4 ,-4}
#
#  NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.


class Solution:

  @staticmethod
  def solution(n):
        hash_map = {}
        res = []
        max_len = 0
        curr_sum = 0
        for i in range(len(n)):
            curr_sum += n[i]
            if n[i] == 0 and max_len == 0:
                max_len = 1
                res = n[i]
            if curr_sum == 0:
                max_len = i + 1
                res.append(n[i])
            if curr_sum in hash_map:
                if max_len < i - hash_map[curr_sum]:
                    print('here')
                    max_len = i - hash_map[curr_sum]
                    print(i - hash_map[curr_sum])
                    res = n[hash_map[curr_sum]+1: i+1]
            else:
                hash_map[curr_sum] = i
        print(res)
        return max_len
number = [1, 2, 3, 0]
res1 = Solution.solution(number)
print(res1)

