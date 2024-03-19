# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        oddListHead = None
        evenListHead = None
        count = 1
        while (head):
            if count % 2 and oddListHead is None:
                oddList = ListNode()
                oddList.val = head.val
                oddListHead = oddList
            elif count % 2 == 0 and evenListHead is None:
                evenList = ListNode()
                evenList.val = head.val
                evenListHead = evenList
            elif count % 2:
                oddList.next = ListNode()
                oddList.next.val = head.val
                oddList = oddList.next
            else:
                evenList.next = ListNode()
                evenList.next.val = head.val
                evenList = evenList.next
            count += 1
            head = head.next
        if(oddListHead is not None and evenListHead is not None):
            oddList.next = evenListHead

        return oddListHead
