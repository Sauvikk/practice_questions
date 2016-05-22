# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# The digit 0 maps to 0 itself.
# The digit 1 maps to 1 itself.
#
# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Make sure the returned strings are lexicographically sorted.
# http://www.programcreek.com/2014/04/leetcode-letter-combinations-of-a-phone-number-java/

class Solution:

  def get_string(self, digits, step, temp, map, result):
            if step == len(digits):
                result.append(''.join(temp))
                return
            curr_char = digits[step]
            curr_str = map[curr_char]
            for i in range(len(curr_str)):
                temp.append(curr_str[i])
                self.get_string(digits, step+1, temp, map, result)
                temp.pop(len(temp) - 1)

  def solution(self, digits):
            map = {'0': "0", '1': "1", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
            result = []
            if digits is None or len(digits) == 0:
                return digits
            temp = []
            self.get_string(digits, 0, temp, map, result)
            return result


res1 = Solution().solution("23")
print(res1)

