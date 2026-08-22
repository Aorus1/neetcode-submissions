class Solution:
    def rob(self, nums: List[int]) -> int:

        dp_0 = 0
        dp_1 = 0
        for num in nums:
            temp = max(num + dp_0, dp_1)
            dp_0 = dp_1
            dp_1 = temp
        return dp_1


        