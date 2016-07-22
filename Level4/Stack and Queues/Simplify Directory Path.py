# Given an absolute path for a file (Unix-style), simplify it.
#
# Examples:
#
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.


class Solution:

  @staticmethod
  def solution(path):
        stack = []
        path = path.split('/')
        for a in path:
            if a == '..':
                if len(stack) > 0:
                    stack.pop()
            elif a == '.':
                continue
            elif len(a) != 0:
                stack.append(a)
        return '/'+'/'.join(stack)


arr = "/home//foo/"
res = Solution.solution(arr)
print(res)

# any language solution
# def solution(path):
#         currrName = ""
#         resWords = []
#         if path[-1] != '/':
#             path += '/'
#
#         for char in path:
#             if char == '/':
#                 if len(currrName) == 0:
#                     continue
#                 if currrName == '..':
#                     if len(resWords) > 0:
#                         resWords.pop()
#                 elif currrName == '.':
#                         None
#                 else:
#                     resWords.append(currrName)
#                 currrName = ""
#             else:
#                 currrName += char
#         res = []
#         if len(resWords) == 0:
#             return '/'
#         for word in resWords:
#             res.append('/' + word)
#         return ''.join(res)
