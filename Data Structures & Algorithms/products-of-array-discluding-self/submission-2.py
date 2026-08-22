from itertools import accumulate
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate([1] + nums[:-1], operator.mul))
        suffix = list(accumulate([1] + nums[:0:-1], operator.mul))[::-1]
        return [p * s for p, s in zip(prefix, suffix)]

        