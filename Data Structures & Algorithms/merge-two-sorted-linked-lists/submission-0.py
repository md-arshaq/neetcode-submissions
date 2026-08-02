# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode(0)
        res = Dummy

        h1 = list1
        h2 = list2

        while h1 and h2:
            if h1.val<=h2.val:
                res.next = ListNode(h1.val)
                h1 = h1.next
            else:
                res.next = ListNode(h2.val)
                h2 = h2.next
            res = res.next

        if h1:
            res.next = h1
        if h2:
            res.next = h2
        
        return Dummy.next