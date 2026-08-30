class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        l = 0
        r = n * m - 1
        while l <= r:
            mid = ((l+r)//2)
            a, b = (mid//n, mid % n)
            if mat[a][b] == target:
                return True
            if mat[a][b] > target:
                r = mid-1
            else:
                l = mid+1
        return False
