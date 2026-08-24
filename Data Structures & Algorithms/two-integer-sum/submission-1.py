class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hm = defaultdict(int)
        for i in range(n):
            if nums[i] in hm:
                return [hm[nums[i]], i]
            hm[target-nums[i]] = i
        

        