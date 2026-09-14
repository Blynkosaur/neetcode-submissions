class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(r,c):
            for dx, dy in dirs:
                px, py = dx + r, dy + c
                if px in range(rows) and py in range(cols) and (px, py) not in visited and board[px][py] == "O":
                    visited.add((px, py))
                    dfs(px,py)
        #top and bottom row
        for i in range(cols):
            if board[0][i] == "O" and (0, i) not in visited:
                visited.add((0,i))
                dfs(0,i)
            if board[rows-1][i] == "O" and (rows-1, i) not in visited:
                visited.add((rows - 1, i))
                dfs(rows-1, i)
        #first and last column
        for i in range(rows):
            if board[i][0] == "O" and (i, 0) not in visited:
                visited.add((i,0))
                dfs(i,0)
            if board[i][cols-1] == "O" and (i, cols - 1) not in visited:
                visited.add((i, cols-1))
                dfs(i, cols-1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
 



            
        