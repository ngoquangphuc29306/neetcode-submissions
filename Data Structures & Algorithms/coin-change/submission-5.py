class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(cur):
            if cur == amount:
                return 0

            if cur in cache:
                return cache[cur]

            minCoin = float('inf')
            for coin in coins:
                if cur + coin <= amount:
                    minCoin = min(minCoin, 1 + dfs(cur + coin))
            
            cache[cur] = minCoin
            return minCoin

        res = dfs(0)

        return -1 if res == float('inf') else res
