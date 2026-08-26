class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = l + ((r-l)//2)
            if (nums[mid] == target): #early return, found
                return mid

            if (target > nums[mid]): # search again on right half
                l = mid+1
            else: # search on left half
                r = mid-1
        return -1

    # nums=[-1,0,2,4,6,8]
    #        0 1 2 3 4 5
    #        l   m     r
    #              l m r