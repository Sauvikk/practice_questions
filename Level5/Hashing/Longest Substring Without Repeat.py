# Given a string,
# find the length of the longest substring without repeating characters.
#
# Example:
#
# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#
# For "bbbbb" the longest substring is "b", with the length of 1.
# http://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# can be done using hash_maps also


class Solution:

  @staticmethod
  def solution(string):
        n = len(string)
        curr_len = 1
        max_len = 1
        prev_index = 0
        i = 0
        visited = [-1] * 256
        visited[ord(string[0])] = 0
        for i in range(1, n):
            prev_index = visited[ord(string[i])]

            if prev_index == -1 or i - curr_len > prev_index:
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = i - prev_index
            visited[ord(string[i])] = i

        if curr_len > max_len:
            max_len = curr_len
        return max_len
s = "asdasdasdaccdgsAawrsf"
res1 = Solution.solution(s)
print(res1)
