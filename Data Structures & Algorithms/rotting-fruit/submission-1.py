class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0,1,2

        row, col = len(grid), len(grid[0])

        q = deque()

        good = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == FRESH:
                    good+= 1
                elif grid[r][c] == ROTTEN:
                    q.append((r,c))
        if good == 0:
            return 0
        
        minutes = -1
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            q_size= len(q)
            minutes += 1

            for _ in range(q_size):
                r,c = q.popleft()
                for dr, dc in directions:
                    nc = c + dc
                    nr = r + dr
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN    
                        good -= 1
                        q.append((nr,nc))
        if good == 0:
            return minutes
        else:
            return -1
            
