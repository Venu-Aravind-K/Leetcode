# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        L = []
        while cur:
            L.append(cur.val)
            cur = cur.next
        dup = []
        for i in range(len(L)-1):
            if L[i] == L[i+1]:
                dup.append(L[i])
        cur = ListNode(-1)
        res = cur
        for i in range(len(L)):
            if L[i] in dup:
                continue
            else:
                cur.next = ListNode(L[i])
                cur = cur.next
        return res.next
