class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amountLeft):
            if amountLeft in memo:
                return memo[amountLeft]
            #base case
            if amountLeft == 0:
                return 0
            if amountLeft < 0:
                return float('inf')

            best = float('inf')
            for n in coins:
                best = min(best, 1 + dfs(amountLeft - n))
                
            memo[amountLeft] = best
            return best

        
        res = dfs(amount)
        if res < float('inf'):
            return res

        return -1
        
            