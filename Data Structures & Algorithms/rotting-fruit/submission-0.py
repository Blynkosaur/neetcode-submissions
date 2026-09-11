class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, remaining = 0, 0
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    remaining += 1  
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        while q:
            x,y,t = q.popleft()
            time = max(t, time)
            for dx, dy in dirs:
                px, py = dx + x, dy + y
                if px in range(rows) and py in range(cols) and grid[px][py] == 1 and (px,py) not in visited:
                    remaining -= 1
                    q.append((px,py, t + 1))
                    visited.add((px,py))
        if remaining:
            return -1
        else:
            return time
    
        