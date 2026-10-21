class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        #bfs
        queue = collections.deque()

        #count the number of fresh oranges, put rotten oranges in stack
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        #now, bfs until all oranges rot, or until queue is empty
        time = 0
        while fresh > 0 and queue:
            next_queue = collections.deque()
            while queue:
                i, j = queue.popleft()
                orng = grid[i][j]

                #top
                if i - 1 > -1 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh -= 1
                    next_queue.append((i - 1, j))

                #bottom
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh -= 1
                    next_queue.append((i + 1, j))

                #right
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh -= 1
                    next_queue.append((i, j + 1))
                #left
                if j - 1 > -1 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh -= 1
                    next_queue.append((i, j - 1))
            queue = next_queue
            time += 1


        if fresh > 0:
            return -1
        return time

        