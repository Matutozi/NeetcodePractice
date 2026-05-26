class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, cols = len(grid), len(grid[0])

        fresh =0
        q= deque()

        #to count the rotten and fresh fruit
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nc = c+dc
                    nr = r+dr

                    if  0 <= nc < cols and 0 <= nr < row and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                    
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1



