# Please Note:
#
# Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.
#
# Please think of all the corner cases and clarifications yourself.
#
# Validate if a given string is numeric.
#
# Examples:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:
    # @param s, a string
    # @return a boolean
    # @finite automation
    def isNumber(self, A):
        A = A.strip()
        n = len(A)
        if n == 0:
            return 0
        if A[0] == '+' or A[0] == '-':
            A = A[1:]
            n -= 1
            if n == 0:
                return 0
        i = 0
        dotEncountered = False
        eEncountered = False
        while i < n:
            if A[i] >= '0' and A[i] <= '9':
                i += 1
                continue
            if A[i] == '.':
                if dotEncountered:
                    return 0
                dotEncountered = True
                i += 1
                if i >= n:
                    return 0
                elif A[i] == 'e':
                    return 0
            elif A[i] == 'e':
                if eEncountered:
                    return 0
                eEncountered = True
                dotEncountered = True
                i += 1
                if i >= n:
                    return False
                if i < n and (A[i] == '-' or A[i] == '+'):
                    i += 1
            else:
                return 0
        return 1


res = Solution().isNumber('2e')
print(res)








# def isNumber(self, s):
#         INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
#         # 0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
#         transitionTable=[[-1,  0,  3,  1,  2, -1],    # 0 no input or just spaces
#                          [-1,  8, -1,  1,  4,  5],    # 1 input is digits
#                          [-1, -1, -1,  4, -1, -1],    # 2 no digits in front just Dot
#                          [-1, -1, -1,  1,  2, -1],    # 3 sign
#                          [-1,  8, -1,  4, -1,  5],    # 4 digits and dot in front
#                          [-1, -1,  6,  7, -1, -1],    # 5 input 'e' or 'E'
#                          [-1, -1, -1,  7, -1, -1],    # 6 after 'e' input sign
#                          [-1,  8, -1,  7, -1, -1],    # 7 after 'e' input digits
#                          [-1,  8, -1, -1, -1, -1]]    # 8 after valid input input space
#         state=0; i=0
#         while i<len(s):
#             inputtype = INVALID
#             if s[i]==' ': inputtype=SPACE
#             elif s[i]=='-' or s[i]=='+': inputtype=SIGN
#             elif s[i] in '0123456789': inputtype=DIGIT
#             elif s[i]=='.': inputtype=DOT
#             elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT
#
#             state=transitionTable[state][inputtype]
#             if state==-1: return False
#             elif inputtype == DOT and i == len(s)-1: return False
#             elif inputtype == DOT and s[i+1] not in "0123456789": return False
#             else: i+=1
#         return state == 1 or state == 4 or state == 7 or state == 8