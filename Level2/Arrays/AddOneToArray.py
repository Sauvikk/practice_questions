class Solution:

  @staticmethod
  def solution(a):
        flag = True
        for i in range(len(a)-1, -1, -1):
            if flag is True:
                 if a[i] == 9:
                        a[i] = 0
                        if i == 0:
                            a.insert(0, 1)
                 else:
                        a[i] += 1
                        flag = False

        while a[0] == 0:
            del a[0]

        return a

a = [0, 0, 4, 4, 6, 0, 9, 6, 5, 1]
res = Solution.solution(a)
print(res)
