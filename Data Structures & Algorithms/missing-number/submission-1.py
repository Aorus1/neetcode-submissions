class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ns = set(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in ns:
                return i