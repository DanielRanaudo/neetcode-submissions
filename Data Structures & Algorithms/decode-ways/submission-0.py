class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        #define dfs function
        def dfs(i):
            #base case, we found the last char
            if i in dp:
                return dp[i]
            #other base case, we see a zero, in which case we cannot continue
            if s[i] == "0":
                return 0
            
            #create a value res, which is the number of decodings from this point onwards
            res = dfs(i + 1)

            #check if the next value creates a valid encoding
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                res += dfs(i + 2)
            
            dp[i] = res
            return res

        return dfs(0)
            
            



        
        