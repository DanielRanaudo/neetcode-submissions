class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #minimum number of coins to get to some value n 
        minAmt = [float('inf')] * (amount + 1)
        minAmt[0] = 0 

        for i in range(len(minAmt)): 
            amountLeft = i
            for j in range(len(coins)):
                coinVal = coins[j]
                if i - coinVal > -1:
                    minAmt[i] = min(minAmt[i], 1 + minAmt[i - coinVal])

        
        if minAmt[amount] != float('inf'):
            return minAmt[amount]
        return -1




        