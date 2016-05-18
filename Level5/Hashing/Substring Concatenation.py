# You are given a string, S, and a list of words, L, that are all of the same length.
#
# Find all starting indices of substring(s) in S that is a concatenation of each word in
# L exactly once and without any intervening characters.
#
# Example :
#
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).


class Solution:

  @staticmethod
  def solution(s, words):
        res = []
        if not s or len(s) == 0 or not words or len(words)== 0:
            return res
        map = {}
        for w in words:
            if w in map:
                map[w] += 1
            else:
                map[w] = 1
        length = len(words[0])
        for j in range(length):
            curr_map = {}
            start = j
            count = 0
            i = j
            while i <= len(s) - length:
                sub = s[i: i+length]
                if sub in map:
                    if sub in curr_map:
                        curr_map[sub] += 1
                    else:
                        curr_map[sub] = 1
                    count += 1

                    while curr_map[sub] > map[sub]:
                        left = s[start: start+length]
                        curr_map[left] -= 1
                        count -= 1
                        start += length
                    if count == len(words):
                        res.append(start)
                        left = s[start: start+length]
                        curr_map[left] -= 1
                        count -= 1
                        start += length
                else:
                    curr_map.clear()
                    start = i + length
                    count = 0
                i += length
        return res
s1 = "geeksforgeeks"
l1 = ["geek", "sfor"]
res1 = Solution.solution(s1, l1)
print(res1)
