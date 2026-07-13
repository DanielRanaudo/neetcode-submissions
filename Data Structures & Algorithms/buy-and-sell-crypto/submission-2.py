class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        cheapest = prices[0]
        res = 0
        for n in prices:
            if n - cheapest > res:
                res = n - cheapest
            elif n < cheapest: 
                cheapest = n
                
            
        return res
            


        