from fractions import Fraction

class Solution:
    # @param A : tuple of integers
    # @return an integer
    @staticmethod
    def solution(arr1, arr2):
            res = []
            i = 0
            j = 0
            size1 = len(arr1)
            size2 = len(arr2)
            while i < size1 and j < size2:
                    if arr1[i] < arr2[j]:
                        res.append(arr1[i])
                        i += 1
                    elif arr2[j] < arr1[i]:
                        res.append(arr2[j])
                        j += 1
                    else:
                        res.append(arr2[j])
                        i += 1
                        j += 1
            while i < size1:
                    res.append(arr1[i])
                    i += 1
            while j < size2:
                    res.append(arr2[j])
                    j += 1
            return res

arr1 = [1, 2, 3]
arr2 = [2, 3]
res = Solution.solution(arr1, arr2)
print(res, res)


