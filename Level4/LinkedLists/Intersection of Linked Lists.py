# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
#  Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

from Level4.LinkedLists.LinkedList import LinkedList


class Solution:

  def solution(self, headA, headB):
        lenA = self.getcount(headA)
        lenB = self.getcount(headB)
        if lenA > lenB:
            d = lenA - lenB
            return self.getIntersectionNode(d, headA, headB)
        else:
            d = lenB - lenA
            return self.getIntersectionNode(d, headB, headA)

  def getIntersectionNode(self, d, node1, node2):
        current1 = node1
        current2 = node2
        for i in range(d):
            if current1 is None:
                return None
            current1 = current1.next
        while current1 and current2:
            if current1.val == current2.val:
                return current1.val
            current1 = current1.next
            current2 = current2.next
        return None

  def getcount(self, node):
        current = node
        count = 0
        while current:
                current = current.next
                count += 1
        return count

A = LinkedList()
B = LinkedList()
A.add(0)
A.add(10)
A.add(20)
A.add(30)
A.add(40)
A.add(50)
A.add(60)
A.add(70)
B.add(0)
B.add(10)
B.add(20)
B.add(30)
B.add(40)
B.add(50)
B.add(63)
res = Solution().solution(A.get_root(), B.get_root())
print(res)
