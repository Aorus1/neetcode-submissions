class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targ = {}
        for i in range(len(nums)):
            if nums[i] in targ:
                return [targ[nums[i]], i]
            targ[target-nums[i]] = i
        
