#Problem 203

class Solution(object):
    def removeElements(self, head, val):
      
        temp = ListNode(0)
        temp.next = head
        prev, curr = temp, head
        while curr:
            if curr.val == val:prev.next = curr.next
            else:prev = curr
            curr = curr.next