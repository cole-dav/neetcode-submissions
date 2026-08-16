class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        column = len(grid[0])

        directions = [[0,1],[0,-1], [-1,0],[1,0]] 
        def dfs(r,c):
            if not (0<= r < rows and 0 <= c < column):
                return 
            if grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr, c+dc)


        for r in range(rows):
            for c in range(column):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res +=1
        return res
            

        