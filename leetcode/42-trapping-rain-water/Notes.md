# Two Pointers Approach

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- Water contained between two pointers = min(maxL, maxR) - height[i]

The algorithm works as follows:

```python
while L < R:
    if maxL < maxR:
        L += 1
        maxL = max(maxL, height[L])
        res += maxL - height[L]
    else:
        R -= 1
        maxR = max(maxR, height[R])
        res += maxR - height[R]
