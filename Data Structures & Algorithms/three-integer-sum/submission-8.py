class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = sorted(nums)
        print(n)
        for i, v in enumerate(n):
            r = len(n) - 1
            l = min(r-1, i+1)
            if (i >= l):
                continue
            print (i, l, r)
            while l != r:
                if n[i] + n[l] + n[r] > 0:
                    r -= 1
                    continue
                elif n[i] + n[l] + n[r] < 0:
                    l += 1
                    continue
                else:
                    if [n[i], n[l], n[r]] in ans:
                        l += 1
                    else:
                        ans.append([n[i], n[l], n[r]])
                        continue
        return ans
                

                

            

        