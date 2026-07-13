class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }

        for c in s: #Iterates through each char in s
            if c in closeToOpen: #if it is a closed par
                if stack and stack[-1] == closeToOpen[c]: #if top of stack matches the apen bracket
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
            


        