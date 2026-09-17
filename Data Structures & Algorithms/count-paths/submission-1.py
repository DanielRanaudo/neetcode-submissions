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






        #bfs branches, each square has a count of how many BFS iterations have visted it.
        res = [[0] * n for _ in range(m)]
        q = [(0, 0)]

        while stack:
            y, x = q.pop()
            res[y][x] += 1
            
            #check for valid movement
            #down
            if (y + 1 < m):
                q.append((y + 1, x))
            if (x + 1 < n):
                q.append((y, x + 1))

        return res[m - 1][n - 1]

        