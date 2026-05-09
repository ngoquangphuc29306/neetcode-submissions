class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for x in nums:
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1
        for val, freq in cnt.items():
            if freq > 1:
                return True
        return False 