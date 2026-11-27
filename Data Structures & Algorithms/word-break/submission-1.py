class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #create a set with all the words in wordDict for quick lookup 
        words = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True 
                    break 

        return dp[len(s)]