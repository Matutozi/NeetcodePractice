class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        atlantic = set()
        pacific =  set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c,visit):
            if (r,c) in visit:
                return 

            visit.add((r,c))
            for dr, dc in directions:
                nc = c + dc
                nr = r + dr

                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr,nc,visit)

        for c in range(cols):
            dfs(0,c,pacific)
        
        for r in range(rows):
            dfs(r,0, pacific)

        for r in range(rows):
            dfs(r,cols-1, atlantic)
        
        for c in range(cols):
            dfs(rows-1, c, atlantic)

        result = []

        for r,c in atlantic & pacific:
            result.append([r,c])
        return result

