class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]
        res[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r + 1 < m:
                    res[r + 1][c] += res[r][c]
                if c + 1 < n: 
                    res[r][c + 1] += res[r][c]

        
        return res[m - 1][n - 1]