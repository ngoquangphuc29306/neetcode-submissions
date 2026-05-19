class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        v = []
        for key, value in cnt.items():
            v.append((key, value))
        v.sort(key = lambda x : x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(v[i][0])
        return res