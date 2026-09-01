class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prevPrev = 1

        for i in range(n - 1):
            temp = prev
            prev += prevPrev
            prevPrev = temp
        

        return prev



        