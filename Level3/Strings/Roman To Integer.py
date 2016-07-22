# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Read more details about roman numerals at Roman Numeric System
#
# Example :
#
# Input : "XIV"
# Return : 14
# Input : "XX"
# Output : 20


class Solution:

  @staticmethod
  def solution(string):
        res = 0
        pre = ' '
        for i in range(len(string)):
            if string[i] == 'M' and pre != 'C': res += 1000
            if string[i] == 'C' and pre != 'X': res += 100
            if string[i] == 'X' and pre != 'I': res += 10
             
            if string[i] == 'M' and pre == 'C': res += 800
            if string[i] == 'C' and pre == 'X': res += 80
            if string[i] == 'X' and pre == 'I': res += 8
             
            if string[i] == 'I': res+=1
             
            if string[i] == 'V' and pre != 'I': res += 5
            if string[i] == 'L' and pre != 'X': res += 50
            if string[i] == 'D' and pre != 'C': res += 500
             
            if string[i] == 'V' and pre == 'I': res += 3
            if string[i] == 'L' and pre == 'X': res += 30
            if string[i] == 'D' and pre == 'C': res += 300
             
            pre = string[i]

        return res

string = "XXIX"
res = Solution.solution(string)
print(res)
