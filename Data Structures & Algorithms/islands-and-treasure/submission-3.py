class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

                   
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j,0))
        while q:
            
            x, y, d = q.popleft()
            # print(x,y,d)

            #sets the value to min 
            grid[x][y] = min(d, grid[x][y])

            for dx, dy in dirs:
                px, py = x + dx, y + dy
                if (px,py) not in visited and px in range(rows) and py in range(cols) and grid[px][py] > 0:
                    q.append((px,py,d + 1))
                    visited.add((px,py))
 
            
            



                
