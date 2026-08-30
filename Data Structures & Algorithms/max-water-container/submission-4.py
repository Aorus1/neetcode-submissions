class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0, n-1

        res = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            res = max(res, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return res
        