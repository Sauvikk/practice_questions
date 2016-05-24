# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:
#
# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]


class Solution:

  def permute(self, numbers, pos, temp, result):
        if pos == len(numbers):
            if temp not in result:
                result.append(temp[:])
            return
        self.permute(numbers, pos + 1, temp, result)
        temp.append(numbers[pos])
        self.permute(numbers, pos + 1, temp, result)
        temp.pop()

  def solution(self, numbers):
        result = []
        if not numbers or len(numbers) == 0:
            return [[]]
        numbers.sort()
        temp = []
        self.permute(numbers, 0, temp, result)
        return sorted(result)

 # def solution(self, s):
 #        s.sort()
 #        r = [[]]
 #        for e in s:
 #            for x in r:
 #                temp = [x + [e]]
 #                if temp not in r:
 #                    r.append(temp[:])
 #        return sorted(r)

res1 = Solution().solution([1, 2, 2])
print(res1)
