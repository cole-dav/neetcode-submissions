class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for val in range(1, 1+ amount):
            for coin in coins:
                if coin <= val:
                    dp[val] = min(dp[val], dp[val - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1