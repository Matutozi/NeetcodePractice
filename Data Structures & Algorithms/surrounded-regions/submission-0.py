class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, cols = len(board), len(board[0])

        zero = list()
        direction = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= cols:
                return

            if board[r][c] != "O":
                return 
            
            board[r][c] = "S"


            for br,bc in direction:
                nr = r + br
                nc = c + bc
                
                dfs(nr,nc)
            
    

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
        for r in range(row):
            if board[r][0] == "O":
                dfs(r,0)

        for r in range(row):
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        for c in range(cols):
            if board[row-1][c] == "O":
                dfs(row-1,c)

        for r in range(row):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"



        
