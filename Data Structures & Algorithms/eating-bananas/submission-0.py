class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mink = r
        while l <= r:
            m = (l + r)//2
            if sum([-(x // -m) for x in piles]) > h:
                l = m + 1
            else:
                mink = min(m, mink)
                r = m - 1
        return mink
