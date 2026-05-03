class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in cnt:
                return [cnt[need], i]
            cnt[nums[i]] = i
        return []