class Solution:
    def longestPalindrome(self, s: str) -> str:
        #odd case
        def helper(i) -> int:
            size = 1
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                size += 2
                l -= 1
                r += 1

            return size
        #even helper
        def helper2(i) -> int:
            if i + 1 >= len(s) or s[i] != s[i+1]:
                return 1
            size = 2
            l, r = i - 1, i + 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                size += 2
                l -= 1
                r += 1
            return size


        #odd case
        maxim = 0
        stringy = ""
        for i in range(len(s)):
            currLen = helper(i)
            if currLen > maxim:
                maxim = currLen
                check = (currLen - 1) // 2
                stringy = s[i - check: i + check + 1]

        
        maxim2 = 0
        string2 = ""
        for i in range(len(s)):
            currLen = helper2(i)
            if currLen > maxim2:
                maxim2 = currLen
                check = (currLen - 2) // 2
                string2 = s[i - check: i + check + 2] 

        if maxim2 > maxim:
            return string2
        return stringy

        
            

        