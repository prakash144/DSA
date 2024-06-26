class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        res = 0

        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, height[L])
                res += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                res += maxR - height[R]

        return res
