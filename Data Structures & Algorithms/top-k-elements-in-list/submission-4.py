from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = list(Counter(nums).items())
        cnt.sort(key = lambda x : x[1], reverse = True)
        res = []
        for i in range(k):
            res.append((cnt[i][0]))
        return res
