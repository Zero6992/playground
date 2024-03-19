# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = None
        while(head):
            current = head
            head = head.next
            current.next = prev
            prev = current
        
        return current
    

