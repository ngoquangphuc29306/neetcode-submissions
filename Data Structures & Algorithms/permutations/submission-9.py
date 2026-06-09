class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])   # phải copy path
                return

            for i in range(len(nums)):
                if used[i] == False:
                    used[i] = True
                    path.append(nums[i])

                    backtrack()

                    path.pop()
                    used[i] = False

        backtrack()
        return res