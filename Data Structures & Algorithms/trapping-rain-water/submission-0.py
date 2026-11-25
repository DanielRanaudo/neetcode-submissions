class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        i = 0
        while i < len(height) and height[i] == 0:
            i += 1
        if i == len(height):
            return 0

        height = height[i:]
        stack = [(height[0], 0)]
        

        tot = 0
        for i in range(1, len(height)):
            curr = height[i]
            stackVal, ind = stack[-1]  #value of top of stack
            while stack and curr >= stackVal:
                stack.pop()
            
                if stack:
                    tot += (i - stack[-1][1] - 1) * (min(curr, stack[-1][0]) - stackVal)
                    stackVal, ind = stack[-1]
                
            stack.append((curr, i))
        return tot


                

        