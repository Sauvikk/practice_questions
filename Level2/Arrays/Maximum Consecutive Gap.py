# http://cgm.cs.mcgill.ca/~godfried/teaching/dm-reading-assignments/Maximum-Gap-Problem.pdf
# http://www.programcreek.com/2014/03/leetcode-maximum-gap-java/


class Bucket:
    def __init__(self, low=-1, high=-1):
        self.low = low
        self.high = high


class Solution:

  @staticmethod
  def solution(num):
        if not num or len(num) < 2:
            return 0
        maximum = num[0]
        minimum = num[0]
        for i in range(1, len(num)):
            maximum = max(maximum, num[i])
            minimum = min(minimum, num[i])

        buckets = []*len(num)
        for i in range(len(num)+1):
            buckets.append(Bucket())

        interval = len(num)/(maximum - minimum)
        print(interval)

        for i in range(len(num)):
            index = int((num[i] - minimum) * interval)
            print(index)
            if buckets[index].low == -1:
                # print(buckets[index].low)
                buckets[index].low = num[i]
                buckets[index].high = num[i]
            else:
                buckets[index].low = min(buckets[index].low, num[i])
                buckets[index].high = max(buckets[index].high, num[i])
        result = 0
        prev = buckets[0].high
        for i in range(len(buckets)):
            if buckets[i].low != -1:
                result = max(result, buckets[i].low-prev)
                prev = buckets[i].high
        return result


a = [ 100, 100, 100, 100, 100 ]
res = Solution.solution(a)
print(res)
