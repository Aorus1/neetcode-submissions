class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        print(setnums)
        maxCons = 0
        for i, num in enumerate(nums):
            currCons = 0
            if not num - 1 in setnums:
                currCons += 1
                while (num+1 in setnums):
                    num += 1
                    currCons += 1
                maxCons = max(maxCons, currCons)
        return maxCons



        