class Solution:

  @staticmethod
  def solution(a):
        curr_sum = 0
        max_so_far = 0
        start = 0
        end = 0
        startmax = -1
        endmax = -1

        for end in range(len(a)):
            if a[end] >= 0:
                curr_sum += a[end]
                if curr_sum > max_so_far:
                    max_so_far = curr_sum
                    startmax = start
                    endmax = end+1
                elif curr_sum == max_so_far:
                    if (end+1-start) > (endmax-startmax):
                        startmax = start
                        endmax = end+1
            else:
                start = end+1
                curr_sum = 0

        res = []
        if startmax == -1 or endmax == -1:
            return res

        for i in range(startmax, endmax):
            res.append(a[i])

        return res

a = [2, 3, 4, -7, 1, 5, 1, 2]
res = Solution.solution(a)
print(res)
