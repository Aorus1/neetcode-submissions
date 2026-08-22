from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return([reduce(lambda a, b: a * b, [x for x in nums[:i] + nums[i+1:]]) for i in range(len(nums))])

        