class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens: 
            if n == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif n == "-":
                secondVal = stack.pop()
                first = stack.pop()
                stack.append(first - secondVal)
                
            elif n == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
                
            elif n == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            elif -200 <= int(n) <= 200:
                stack.append(int(n))
                
        
        return stack.pop()



        