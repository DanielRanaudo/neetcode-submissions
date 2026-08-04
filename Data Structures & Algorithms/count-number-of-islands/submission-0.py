class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs/dfs, count the number of times we have to restart
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        total = 0

        def explore(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == "0":
                return
            visited.add((r, c))
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    explore(r, c)
                    total += 1
        
        

        return total
