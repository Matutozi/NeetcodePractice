class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, coln = len(grid), len(grid[0])

        visit = set()

        island = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= coln or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1,col)
            dfs(row-1, col)

        

        for r in range(rows):
            for c in range(coln):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island += 1
        return island