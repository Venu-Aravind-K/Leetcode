# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = []
        Cur = head
        while Cur:
            if Cur in L:
                return Cur
            L.append(Cur)
            Cur = Cur.next
        return None 