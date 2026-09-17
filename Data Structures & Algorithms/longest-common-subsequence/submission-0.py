class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            char1 = text1[i]
            for j in range(len(text2)):
                
                char2 = text2[j]
                if char1 == char2: 
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else: 
                     top = dp[i - 1][j] if i > 0 else 0
                     left = dp[i][j - 1] if j > 0 else 0
                     dp[i][j] = max(top, left)
                


        return dp[len(text1) - 1][len(text2) - 1]
