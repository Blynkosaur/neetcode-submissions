class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_visited = set()
        a_visited = set()
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols = len(heights), len(heights[0])
        def dfs(r,c, sea):
            s = p_visited if sea == "p" else a_visited 
            for dx, dy in dirs:
                px,py = dx + r, dy + c
                if px in range(rows) and py in range(cols) and heights[px][py] >= heights[r][c] and (px,py) not in s:
                    s.add((px,py))
                    dfs(px, py, sea)
        for i in range(cols):
            if (0, i) not in p_visited:
                p_visited.add((0,i))
                dfs(0,i, "p")
        for i in range(rows):
            if (i, 0) not in p_visited:
                p_visited.add((i,0))
                dfs(i, 0, "p")
        for i in range(cols):
            if (rows-1, i) not in a_visited:
                a_visited.add((rows-1, i))
                dfs(rows-1, i, "a")
        for i in range(rows):
            if (i, cols-1) not in a_visited:
                a_visited.add((i, cols-1))
                dfs(i, cols -1, "a")
        

        return list(p_visited & a_visited)

        
        