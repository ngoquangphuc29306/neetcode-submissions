class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum // 2

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for s in range(1, target + 1):
                # un select nums[i]
                dp[i][s] = dp[i - 1][s]

                # Select nums[i]
                if s >= nums[i - 1]:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - nums[i - 1]]
        return dp[n][target]