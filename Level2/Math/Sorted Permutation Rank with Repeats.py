import math


class Solution:

  @staticmethod
  def solution(s):
        dict = {}
        n = len(s)
        rank = 1
        for i in range(n):
            if s[i] not in dict.keys():
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        print(dict)
        for i in range(n-1):
            x = 0
            for j in range(i+1, n):
                if s[i] > s[j]:
                    x += 1
            rank += x * math.factorial(n-i-1)
            for key in dict.keys():
                if key == s[i]:
                    if dict[s[i]] != 1:
                        print('here')
                        dict[s[i]] -= 1
                rank = int(rank/math.factorial(dict[key]))
            rank %= 1000003
        return rank

s = "baa"
output = Solution.solution(s)
print(output)


# http://stackoverflow.com/questions/22642151/finding-the-ranking-of-a-word-permutations-with-duplicate-letters
# def findRank(self, perm):
#        rank = 1
#        suffixperms = 1
#        ctr = Counter()
#        for i in range(len(perm)):
#            x = perm[((len(perm) - 1) - i)]
#            ctr[x] += 1
#            for y in ctr:
#                if (y < x):
#                    rank += ((suffixperms * ctr[y]) // ctr[x])
#            suffixperms = ((suffixperms * (i + 1)) // ctr[x])
#            rank %= 1000003
#        return rank

