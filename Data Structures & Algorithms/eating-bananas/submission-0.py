class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        while l < r:
            middle = (l + r) // 2 ##hourly rate
            hours_spent = 0

            for p in piles:
                hours_spent += math.ceil(p / middle)
            
            if hours_spent <= h: #went through quick, could go slower
                r = middle
            if hours_spent > h:
                l = middle + 1
        
        return r
