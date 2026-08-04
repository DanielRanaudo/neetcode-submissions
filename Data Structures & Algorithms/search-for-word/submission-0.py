class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       #keep track of visited:
        visited = set()

        def dfs(currRow, currCol, pos):
            if pos == len(word):
                return True
            if currRow >= len(board) or currRow < 0 or currCol >= len(board[0]) or currCol < 0 or board[currRow][currCol] != word[pos] or (currRow, currCol) in visited:
                return False
            
            visited.add((currRow, currCol))
            
            #otherwise, call on all 4
            res = ( 
            dfs(currRow, currCol + 1, pos + 1) or #down
            dfs(currRow + 1, currCol, pos + 1) or #right
            dfs(currRow - 1, currCol, pos + 1) or #left
            dfs(currRow, currCol - 1, pos + 1) #up
            )

            

            #remove the current
            visited.remove((currRow, currCol))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
            


    


