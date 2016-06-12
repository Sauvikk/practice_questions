# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) – Push element x onto stack.
# pop() – Removes the element on top of the stack.
# top() – Get the top element.
# getMin() – Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.
#
# Questions to ask the interviewer :
#
# Q: What should getMin() do on empty stack?
# A: In this case, return -1.
#
# Q: What should pop do on empty stack?
# A: In this case, nothing.
#
# Q: What should top() do on empty stack?
# A: In this case, return -1


class minStack:
    s = []
    sMin = []

    def __init__(self):
        self.s = []
        self.sMin = []

    # @param x, an integer
    def push(self, x):
        self.s.append(x)
        if len(self.sMin) == 0 or x <= self.sMin[-1]:
            self.sMin.append(x)

    # @return nothing
    def pop(self):
        if len(self.s) !=0 and len(self.sMin) != 0:
            if self.s[-1] == self.sMin[-1]:
                self.sMin.pop()
            self.s.pop()


    # @return an integer
    def top(self):
        if len(self.s) != 0:
            return self.s[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        if len(self.s) != 0:
            return self.sMin[-1]
        else:
            return -1


minstack = minStack()
minstack.push(19)
minstack.push(10)
minstack.push(9)
print(minstack.getMin())

