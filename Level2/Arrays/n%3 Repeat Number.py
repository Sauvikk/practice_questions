# http://www.cs.utexas.edu/users/moore/best-ideas/mjrty/index.html
# http://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/


class Solution:

  @staticmethod
  def solution(a):
        map = {}
        print(len(a))
        for val in a:
            if val in map.keys():
                print('hahaha')
                map[val] += 1
            else:
                flag = True
                if len(map) == 3:
                    for key in map.keys():
                        if map[key] == 0:
                            map[val] = 0
                            print('in Del', end=',')
                            print(key, val)
                            del map[key]
                            flag = False
                            break
                    if flag is True:
                        for key in map.keys():
                            print('in minus', end=',')
                            print(map[key])
                            map[key] -= 1
                else:
                    map[val] = 0
        res = []
        for key in map.keys():
            ac = 0
            for val in a:
                if val == key:
                    ac += 1
            print(key, ac)
            if ac > (int(len(a)/3)):
                print(ac)
                return key
        print(map)
        return -1
a = [ 1000442, 1000206, 1000956, 1000143, 1000426, 1000592, 1000426, 1000136, 1000654, 1000426, 1000115, 1000121, 1000311, 1000451, 1000265, 1000426, 1000426, 1000254, 1000501, 1000715, 1000635, 1000602, 1000943, 1000119, 1000426, 1000426, 1000426, 1000378, 1000975, 1000292, 1000851, 1000426, 1000426, 1000181, 1000355, 1000426, 1000248, 1000143, 1000426, 1000985, 1000426, 1000634, 1000426, 1000945, 1000880, 1000426, 1000426, 1000135, 1000426, 1000402, 1000156, 1000426, 1000835, 1000599, 1000192, 1000451, 1000426, 1000241, 1000124, 1000100, 1000812, 1000611, 1000426, 1000641, 1000426, 1000426, 1000461, 1000872, 1000973, 1000426, 1000438, 1000517, 1000243, 1000658, 1000738, 1000396, 1000426, 1000426, 1000068, 1000427, 1000426, 1000504, 1000426, 1000462, 1000294, 1000504, 1000421, 1000883, 1000414, 1000426, 1000937, 1000426, 1000426, 1000819, 1000400, 1000323, 1000855, 1000779, 1000353, 1000426, 1000426, 1000506, 1000779, 1000487, 1000696, 1000729, 1000426, 1000025, 1000357, 1000946, 1000101, 1000459, 1000893, 1000426, 1000450, 1000491, 1000049, 1000420, 1000426, 1000103, 1000638, 1000315, 1000011, 1000426, 1000861, 1000111, 1000030, 1000477, 1000454, 1000309, 1000426, 1000756, 1000880, 1000213, 1000426, 1000206, 1000426, 1000436, 1000426, 1000026, 1000426, 1000756, 1000039, 1000426, 1000426, 1000426, 1000686, 1000426, 1000665, 1000426, 1000890, 1000992, 1000235, 1000701, 1000305, 1000482, 1000405, 1000426, 1000282, 1000191, 1000663, 1000199, 1000426, 1000119, 1000901, 1000998, 1000323, 1000426, 1000426, 1000844, 1000032, 1000737, 1000756, 1000426, 1000426, 1000275, 1000426, 1000635, 1000426, 1000426, 1000021, 1000426, 1000426, 1000322, 1000426, 1000501, 1000987, 1000995, 1000567, 1000795, 1000092, 1000758, 1000012, 1000426, 1000196, 1000641, 1000455, 1000426, 1000085, 1000933, 1000730, 1000426, 1000602, 1000549, 1000211, 1000025, 1000986, 1000349, 1000264, 1000426, 1000024, 1000426, 1000426, 1000680, 1000869, 1000320, 1000020, 1000194, 1000426, 1000426, 1000426, 1000716, 1000356, 1000748, 1000201, 1000426, 1000426, 1000002, 1000215, 1000850, 1000184, 1000803, 1000688, 1000561, 1000258, 1000426, 1000426, 1000612, 1000426, 1000246, 1000109, 1000156, 1000426, 1000355, 1000657, 1000929, 1000953, 1000159, 1000426, 1000919, 1000408, 1000778, 1000038, 1000046, 1000300, 1000272, 1000800, 1000426, 1000442, 1000551, 1000825, 1000501, 1000081, 1000426, 1000157, 1000203, 1000426, 1000022, 1000704, 1000426, 1000426, 1000034, 1000426, 1000163, 1000140, 1000426, 1000426, 1000704, 1000880, 1000707, 1000877, 1000214, 1000426, 1000426, 1000675, 1000312, 1000025, 1000426, 1000426, 1000792, 1000426, 1000326, 1000491, 1000633, 1000861, 1000426, 1000693, 1000426, 1000961, 1000647, 1000426, 1000426, 1000426, 1000426, 1000366, 1000871, 1000426, 1000904, 1000998, 1000114, 1000697, 1000426, 1000586, 1000426, 1000026, 1000994, 1000127, 1000205, 1000148, 1000280, 1000778, 1000380, 1000426, 1000122, 1000426, 1000426, 1000702, 1000426, 1000234, 1000426, 1000091, 1000426, 1000483, 1000712, 1000426, 1000425, 1000426, 1000692, 1000847, 1000331, 1000795, 1000328, 1000426, 1000677, 1000094, 1000426, 1000839, 1000890, 1000065, 1000641, 1000426, 1000426, 1000426, 1000463, 1000426, 1000445, 1000415, 1000243, 1000426, 1000426, 1000426, 1000029, 1000426, 1000426, 1000426, 1000572, 1000390, 1000931, 1000413, 1000606, 1000425, 1000426, 1000039, 1000657, 1000069, 1000998, 1000120, 1000426, 1000063, 1000015, 1000396, 1000426, 1000257, 1000397, 1000161, 1000426, 1000426, 1000493, 1000426, 1000501, 1000124, 1000426, 1000424, 1000902, 1000426, 1000426, 1000048, 1000426, 1000426, 1000394, 1000535, 1000426, 1000899, 1000654, 1000778, 1000120, 1000426, 1000426, 1000426, 1000568, 1000677, 1000426, 1000426, 1000723, 1000997, 1000426, 1000934, 1000881, 1000426, 1000687, 1000426, 1000487, 1000426, 1000426, 1000426, 1000131, 1000396, 1000107, 1000902, 1000426, 1000426, 1000525, 1000985, 1000426, 1000255, 1000991, 1000426, 1000426, 1000426, 1000020, 1000426, 1000426, 1000450, 1000455, 1000283, 1000426, 1000426, 1000426, 1000938, 1000426, 1000255, 1000426, 1000248, 1000099, 1000622, 1000426, 1000329, 1000005, 1000826, 1000060, 1000313, 1000426, 1000426, 1000426, 1000662, 1000426, 1000426, 1000426, 1000906, 1000482, 1000426, 1000349, 1000426, 1000968, 1000426, 1000426, 1000239, 1000426, 1000480, 1000357, 1000417, 1000311, 1000510, 1000085, 1000652, 1000426, 1000548, 1000426, 1000426, 1000426, 1000766, 1000751, 1000426, 1000685, 1000695, 1000455, 1000218, 1000426, 1000426, 1000426, 1000426, 1000696, 1000179, 1000506, 1000426, 1000408, 1000812, 1000871, 1000720, 1000144, 1000213, 1000083, 1000931, 1000128, 1000250, 1000426, 1000783, 1000426, 1000149, 1000376, 1000228, 1000426, 1000812, 1000000, 1000685, 1000525, 1000476, 1000826, 1000737, 1000426, 1000130, 1000561, 1000426, 1000281, 1000426, 1000866, 1000453, 1000240, 1000074, 1000426, 1000388, 1000426, 1000794, 1000426, 1000244, 1000426, 1000969, 1000817, 1000036, 1000426, 1000426, 1000490, 1000426, 1000795, 1000050, 1000808, 1000426, 1000426, 1000872, 1000426, 1000668, 1000426, 1000995, 1000140, 1000710, 1000983, 1000929, 1000434, 1000425, 1000019, 1000232, 1000892, 1000426, 1000561 ]
# a =[ 1000382, 1000320, 1000573, 1000320, 1000325, 1000736, 1000320, 1000834, 1000635, 1000467, 1000320, 1000205, 1000320, 1000545 ]
res = Solution.solution(a)
print(res)

# works
# def repeatedNumber(self, a):
#         count = {}
#         for i in a:
#             if i not in count:
#                 count[i] = 1
#             else:
#                 count[i] += 1
#         for i in count:
#             if count[i] > len(a)/3:
#                 return i
#         return -1
