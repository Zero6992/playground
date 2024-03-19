# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        resHead = None
        while(list1 and list2):
            if resHead is None and list1.val <= list2.val:
                res = ListNode()
                res.val = list1.val
                resHead = res
                list1 = list1.next
            elif resHead is None and list1.val > list2.val:
                res = ListNode()
                res.val = list2.val
                resHead = res
                list2 = list2.next
            elif list1.val <= list2.val:
                res.next = ListNode()
                res.next.val = list1.val
                res = res.next
                list1 = list1.next
            elif list1.val > list2.val:
                res.next = ListNode()
                res.next.val = list2.val
                res = res.next
                list2 = list2.next
        
        while(list1):
            if resHead is None:
                res = ListNode()
                res.val = list1.val
                resHead = res
            else:
                res.next = ListNode()
                res.next.val = list1.val
                res = res.next
            list1 = list1.next

        while(list2):
            if resHead is None:
                res = ListNode()
                res.val = list2.val
                resHead = res
            else:
                res.next = ListNode()
                res.next.val = list2.val
                res = res.next
            list2 = list2.next
        
        return resHead