class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #grids are defined as: cols: 0 - 2, 3 - 5, 6 - 8
        #                       rows: 0 - 2, 3- 5, 6 - 8

        #we can first do a pass checking if any of the rows contain dups

        for i in range(len(board)):
            check = set()
            for j in range(len(board[0])):
                if board[i][j] in check:
                    return False 
                elif board[i][j] != ".":
                    check.add(board[i][j])
        
        #now check if the cols contain dups
        for j in range(len(board[0])):
            check = set() 
            for i in range(len(board)):
                if board[i][j] in check:
                    return False
                elif board[i][j] != ".": 
                    check.add(board[i][j])

        #check each of the 9 subtables 
        def check_table(r_start, r_end, c_start, c_end):
            check = set()
            for i in range(r_start, r_end):
                for j in range(c_start, c_end):
                    if board[i][j] in check:
                        return False
                    elif board[i][j] != ".":
                        check.add(board[i][j])
            
            return True

        return (check_table(0, 3, 0, 3) and check_table(0, 3, 3, 6) and check_table(0, 3, 6, 9) and
        check_table(3, 6, 0, 3) and check_table(3, 6, 3, 6) and check_table(3,6, 6, 9) and
        check_table(6, 9, 0, 3) and check_table(6, 9, 3, 6) and check_table(6, 9, 6, 9))




        
                
        