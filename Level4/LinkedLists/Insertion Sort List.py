# Sort a linked list using insertion sort.
#
# We have explained Insertion Sort at Slide 7 of Arrays
#
# Insertion Sort Wiki has some details on Insertion Sort as well.
#
# Example :
#
# Input : 1 -> 3 -> 2
#
# Return 1 -> 2 -> 3

from Level4.LinkedLists.LinkedList import LinkedList, Node




class Solution:

  def solution(self, head):
        # will also work without this as it is handled in the other function
        if not head or not head.next:
            return None
        curr = head
        result = None
        while curr:
            next = curr.next
            result = self.sortedinsert(result, curr)
            curr = next
        return result

  def sortedinsert(self, head, new_node):
        if not head or new_node.val <= head.val:
            new_node.next = head
            return new_node
        else:
            current = head
            while current and new_node.val > current.val:
                prev = current
                current = current.next
            new_node.next = current
            prev.next = new_node
            return head


A = LinkedList()
A.add(0)
A.add(5)
A.add(2)
A.add(3)
A.add(4)
A.add(1)
A.add(1234)
A.add(12)
A.add(18)
A.add(13)
A.add(12)
A.add(1)


A.print()
res = Solution().solution(A.get_root())
LinkedList.print_any(res)
