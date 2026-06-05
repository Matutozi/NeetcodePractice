class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_l = {i:[] for i in range(n)}

        for a,b in edges:
            adj_l[a].append(b)
            adj_l[b].append(a)

        visited = set()
        components = 0
        
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj_l[node]:
                dfs(nei)

        for num in range(n):
            if num not in visited:
                components+=1
                dfs(num)

        return components