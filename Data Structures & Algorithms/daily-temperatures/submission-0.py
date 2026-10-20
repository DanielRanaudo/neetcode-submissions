class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        day = 0
        for i in range(1, len(temperatures)):
            day += 1
            curr_temp = temperatures[i]
            while stack and stack[-1][0] < curr_temp:
                past_temp, past_day = stack.pop()
                res[past_day] = day - past_day 
            stack.append((curr_temp, day))
        
        return res
        