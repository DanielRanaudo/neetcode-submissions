class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "".join(char for char in s if char.isalnum()).lower()
   
        for i in range(len(newString)):
            j = len(newString) - 1 - i
            if j <= i:
                return True
            if newString[i] != newString[j]:
                return False
        return True    