# Prefix Sums Approach

1. Maintain a `prefixCount` hashMap with a default value of `{0:1}`.
2. Increment the result `res` by the value corresponding to `diff` in the `prefixCount` hashMap, or 0 if it doesn't exist.
6. Update `prefixCount` by incrementing the count for `curSum`.

Python code implementing these steps is as follows:

```python
curSum = 0
res = 0
prefixCount = {0: 1}

for n in nums:
    curSum += n
    diff = curSum - k
    res += prefixCount.get(diff, 0)
    prefixCount[curSum] = 1 + prefixCount.get(curSum, 0)
