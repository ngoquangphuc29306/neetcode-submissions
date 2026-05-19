import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        min_heap = []

        for num, freq in cnt.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []

        while min_heap:
            freq, num = heapq.heappop(min_heap)
            res.append(num)

        return res