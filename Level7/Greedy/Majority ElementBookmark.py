# Given an array of size n, find the majority element.
#  The majority element is the element that appears more than floor(n/2) times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example :
#
# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, arr):
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic:
            if dic[key] > int(len(arr)/2):
                return key

# Majority Vote Algorithm
class Solution1:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, arr):
        result = 0
        count = 0
        for num in arr:
            if count == 0:
                result = num
                count = 1
            elif result == num:
                count += 1
            else:
                count -= 1
        return result