# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address must be in the form of A.B.C.D,
# where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
#
# Example:
#
# Given “25525511135”,
#
# return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)


class Solution:

 def solution(self, s):
        res = []
        self.getRes(s, "", res, 4)
        return res

 def valid(self, s):
     n = len(s)
     if n == 3 and (s > '255' or s == '0'): return False
     if n == 3 and s[0] == '0': return False
     if n == 2 and s == '0': return False
     if n == 2 and s[0] == '0': return False
     return True

 def getRes(self, s, r, res, k):
     if k == 0:
         if not s:
             res.append(r)
             return
     else:
         for i in range(1, 4):
             if len(s) >= i and self.valid(s[0: i]):
                 if k == 1:
                     self.getRes(s[i:], r+s[0: i],res, k-1)
                 else:
                     self.getRes(s[i:], r+s[0: i]+".", res, k-1)


string = "25525511135"
res = Solution().solution(string)
print(res)
