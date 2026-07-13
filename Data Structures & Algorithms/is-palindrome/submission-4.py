class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            while not self.isAlphaNum(s[r]) and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True



    def isAlphaNum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))




        newString = "".join(char for char in s if char.isalnum()).lower()
   
        for i in range(len(newString)):
            j = len(newString) - 1 - i
            if j <= i:
                return True
            if newString[i] != newString[j]:
                return False
        return True    