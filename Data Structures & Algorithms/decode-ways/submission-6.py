class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1
        
        for i in range(1, len(s)):
            curr = s[i]
            prev = s[i - 1]
            if prev == '1' or (prev == '2' and '0' <= curr <= '6'):
                dp[i] += dp[i - 2] if i >= 2 else 1   
            if curr != '0':
                dp[i] += dp[i - 1] 

        return dp[len(s) - 1]