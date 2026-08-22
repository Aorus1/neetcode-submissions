class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            current = min(heights[l], heights[r]) * abs(l - r)
            best = max(current, best)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return best


            
        