class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hashmap = {} # map difference to index
        for i, num in enumerate(nums):
            if num in hashmap:
                ans.append(hashmap[num])
                ans.append(i)
                return ans
            else:
                hashmap[target - num] = i
        return ans
        
        