# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        res = 0

        while fast and fast.next:
            fast = fast.next.next
            # Reverse the fist half of LL
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res
