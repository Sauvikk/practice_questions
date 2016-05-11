# You are given two linked lists representing two non-negative numbers. The digits are stored in
# reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.


from Level4.LinkedLists.LinkedList import LinkedList, Node


class Solution:

  @staticmethod
  def solution(first, second):
        prev = None
        temp = None
        head = None
        carry = 0
        res = LinkedList()
        while first or second:
            fdata = 0 if first is None else first.val
            sdata = 0 if second is None else second.val
            sum = carry + fdata + sdata
            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum % 10
            temp = Node(sum)
            if head is None:
                head = temp
            else:
                prev.next = temp
            prev = temp
            if first:
                first = first.next
            if second:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)
        return head

A = LinkedList()
A.add(9)
A.add(9)
A.add(9)
B = LinkedList()
B.add(1)
B.add(0)
A.print()
B.print()
res = Solution.solution(A.get_root(), B.get_root())
LinkedList.print_any(res)
