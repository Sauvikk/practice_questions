# Given two words (start and end), and a dictionary, find the shortest
# transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# If there are multiple such sequence of shortest length, return all of them. Refer to the example for more details.
#
# Example :
#
# Given:
#
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
#  Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

from collections import deque


class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        dictV = set(dictV)
        dictV.add(end)
        queue = deque([(start, 1, [start])])
        visited = set()
        min_length = float('inf')
        ladders = []
        while queue:
            word, length, ladder = queue.popleft()
            visited.add(word)
            if word == end:
                if length == min_length:
                    ladders.append(ladder)
                elif length < min_length:
                    min_length = length
                    ladders = [ladder]
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in dictV and new_word not in visited:
                        queue.append((new_word, length+1, ladder+[new_word]))
        return ladders  # No sequence


start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
print(Solution().findLadders(start, end, dict))