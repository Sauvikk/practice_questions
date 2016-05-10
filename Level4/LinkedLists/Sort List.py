# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example :
#
# Input : 1 -> 5 -> 4 -> 3
#
# Returned list : 1 -> 2 -> 4 -> 5


from Level4.LinkedLists.LinkedList import LinkedList, Node

import sys
sys.setrecursionlimit(2500)


class Solution:

  def sort(self, head, size):
        if size == 1:
            return head
        list2 = head
        for i in range(0, size//2):
            list2 = list2.next
        list1 = self.sort(head, size//2)
        list2 = self.sort(list2, size-size//2)
        return self.merge(list1, size//2, list2, size-size//2)

  def merge(self, list1, sizeList1, list2, sizeList2):
        dummy = Node(0)
        list = dummy
        pointer1 = 0
        pointer2 = 0
        while pointer1 < sizeList1 and pointer2 < sizeList2:
            if list1.val < list2.val:
                list.next = list1
                list1 = list1.next
                pointer1 += 1
            else:
                list.next = list2
                list2 = list2.next
                pointer2 += 1
            list = list.next
        while pointer1 < sizeList1:
            list.next = list1
            list1 = list1.next
            pointer1 += 1
            list = list.next
        while pointer2 < sizeList2:
            list.next = list2
            list2 = list2.next
            pointer2 += 1
            list = list.next
        list.next = None
        return dummy.next

  def sortList(self, head):
        if head == None:
            return None
        counter = 0
        temp = head
        while temp != None:
            temp = temp.next
            counter += 1
        return self.sort(head, counter)


A = LinkedList()
A.add(3)
A.add(4)
A.add(5)
A.add(1)
res = Solution().sortList(A.get_root())
LinkedList.print_any(res)
