class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        a1 = nums[1:]
        a2 = nums[:-1]

        max_money = 0

        n = len(a1)
        rob1, rob2 = 0, 0
        for i in range(n):
            temp = max(rob1 + a1[i], rob2)
            rob1 = rob2
            rob2 = temp
        max_money = rob2

        

        rob1, rob2 = 0, 0
        for i in range(n):
            temp = max(rob1 + a2[i], rob2)
            rob1 = rob2
            rob2 = temp
        return max(max_money, rob2)