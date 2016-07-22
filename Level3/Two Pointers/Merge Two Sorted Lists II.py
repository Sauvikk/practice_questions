# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
#  Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
# TIP: C users, please malloc the result into a new array and return the result.
# If the number of elements initialized in A and B are m and n respectively,
# the resulting size of array A after your code is executed should be m + n
#
# Example :
#
# Input :
#          A : [1 5 8]
#          B : [6 9]
#
# Modified A : [1 5 6 8 9]


class Solution:

  @staticmethod
  def solution(arr1, arr2):
            size1 = len(arr1)
            size2 = len(arr2)
            i = size1 - 1
            j = size2 - 1
            for x in range(size2):
                arr1.append(0)
            count = size1 + size2 - 1
            while i >= 0 and j >= 0:
                    if arr1[i] > arr2[j]:
                        arr1[count] = arr1[i]
                        i -= 1
                        count -= 1
                    else:
                        arr1[count] = arr2[j]
                        j -= 1
                        count -= 1
                    # else:
                    #     arr1[count] = arr1[i]
                    #     i -= 1
                    #     j -= 1
                    #     count -= 1
            while i >= 0:
                    arr1[count] = arr1[i]
                    i -= 1
                    count -= 1
            while j >= 0:
                    arr1[count] = arr2[j]
                    j -= 1
                    count -= 1
            return arr1

arr1 = [1, 2, 3]
arr2 = [2, 3]
res = Solution.solution(arr1, arr2)
print(res)


# union of two arrays
# def solution(arr1, arr2):
#             res = []
#             i = 0
#             j = 0
#             size1 = len(arr1)
#             size2 = len(arr2)
#             while i < size1 and j < size2:
#                     if arr1[i] < arr2[j]:
#                         res.append(arr1[i])
#                         i += 1
#                     elif arr2[j] < arr1[i]:
#                         res.append(arr2[j])
#                         j += 1
#                     else:
#                         res.append(arr2[j])
#                         i += 1
#                         j += 1
#             while i < size1:
#                     res.append(arr1[i])
#                     i += 1
#             while j < size2:
#                     res.append(arr2[j])
#                     j += 1
#             return res
