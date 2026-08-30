class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        l_h, r_h = height[l], height[r]
        water = 0

        while l < r:
            l_h, r_h = max(height[l], l_h), max(height[r], r_h) 
            if height[l] <= height[r]:
                l += 1
                water += max(min(l_h, r_h) - height[l], 0)
            else:
                r -= 1
                water += max(min(l_h, r_h) - height[r], 0)
        return water

            


            

        