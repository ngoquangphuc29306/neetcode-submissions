class Solution:
    def F(self, piles, hours, k):
        ans = 0
        for i in range(len(piles)):
            ans += (piles[i] + k - 1) // k
        return ans <= hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        l = 1
        r = max_k
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if self.F(piles, h, m) == True:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
