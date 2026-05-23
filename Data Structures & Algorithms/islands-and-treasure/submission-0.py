class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])

        q = deque()

        visit = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nc = dc + c
                nr = dr + r

                if (
                    nr < 0 or
                    nc < 0 or
                    nr == row or
                    nc == col or
                    (nr, nc) in visit or
                    grid[nr][nc] == -1
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1

                visit.add((nr, nc))
                q.append((nr, nc))
                

