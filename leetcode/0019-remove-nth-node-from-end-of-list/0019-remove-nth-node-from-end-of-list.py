# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        leftNode = dummyNode
        rightNode = head

        while n > 0 and rightNode:
            rightNode = rightNode.next
            n -= 1

        while rightNode:
            leftNode = leftNode.next
            rightNode = rightNode. next
        

        leftNode.next = leftNode.next.next

        return dummyNode.next