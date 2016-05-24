# Given a string s, partition s such that every string of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")


class Solution:

  def is_palindrom(self, low, high, s):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

  def generate(self, s, pos, temp, result):
        if pos == len(s):
            result.append(temp[:])
            return
        for i in range(pos, len(s)):
            if self.is_palindrom(pos, i, s):
                temp.append(s[pos: i+1])
                self.generate(s, i+1, temp, result)
                temp.pop()

  def solution(self, s):
        result = []
        if not s or len(s) == 0:
            return result
        temp = []
        self.generate(s, 0, temp, result)
        return sorted(result)


res1 = Solution().solution("nitin")
print(res1)
