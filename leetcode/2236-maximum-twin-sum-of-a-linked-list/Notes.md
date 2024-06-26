<h2>maximum-twin-sum-of-a-linked-list Notes</h2><hr>[ Time taken: 8 m 6 s ]

# Fast and Slow Pointers Approach

1. Reverse the first half of the linked list.
2. Traverse the reversed first half and the second half simultaneously.
3. Calculate the maximum twin sum.

You can implement this approach in Python code as follows:

```python

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
