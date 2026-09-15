class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [False] * (len(s) + 1)
        memo[0] = True #empty string can be solved
        

        for i in range(len(s) + 1):
            for j in range(i):
                if memo[j] and s[j:i] in wordSet:
                    memo[i] = True
                    break

        return memo[len(s)]
            
            