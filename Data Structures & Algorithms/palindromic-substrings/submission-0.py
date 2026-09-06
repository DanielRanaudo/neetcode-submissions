class Solution:
    def countSubstrings(self, s: str) -> int:
        #count how many palindromes each char is in, add them up
        dp = [0] * len(s)
        total = 0
        
        #count palindromes for each instance, both even and odd, for even we look at the right
        for i in range(len(s)):
            #add singlechar
            dp[i] += 1
            total += 1

            l = i - 1
            r = i + 1

            #check odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                dp[i] += 1
                dp[l] += 1
                dp[r] += 1
                l -= 1
                r += 1


            #check even 
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                total += 1
                if i == l:
                    dp[i] += 1
                    dp[r] += 1
                else:
                    dp[i] += 1
                    dp[l] += 1
                    dp[r] += 1

                l -= 1
                r += 1

        return total
        #sum all values in dp array
        res = 0
        for n in dp:
            res += n

        return res