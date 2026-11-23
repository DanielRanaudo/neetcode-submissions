class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        def bfs(y, x) -> int:
            deq = deque()
            deq.append((y, x))
            
            area = 0
            while deq:
                y, x = deq.popleft()
                if y - 1 >= 0 and grid[y-1][x] == 1 and ((y - 1, x)) not in visited:
                    deq.append((y-1, x))
                    visited.add((y - 1, x))
                if y + 1 < len(grid) and grid[y + 1][x] == 1 and ((y + 1, x)) not in visited:
                    deq.append((y + 1, x))
                    visited.add((y + 1, x))
                if x - 1 >= 0 and grid[y][x - 1] == 1 and ((y, x - 1)) not in visited:
                    deq.append((y, x - 1))
                    visited.add((y, x - 1))
                if x + 1 < len(grid[0]) and grid[y][x + 1] == 1 and ((y, x + 1)) not in visited:
                    deq.append((y, x + 1))
                    visited.add((y, x + 1))
                area += 1
                
            return area

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and ((i, j)) not in visited:
                    visited.add((i, j))
                    maxArea = max(maxArea, bfs(i, j))
        
        return maxArea








        