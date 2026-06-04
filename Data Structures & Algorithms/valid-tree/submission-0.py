class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        adj_matrix = {i:[] for i in range(n)}
        
        for a,b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)

        visit = set()


        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)

            for neig in adj_matrix[node]:
                if neig == parent:
                    continue
                if not dfs(neig, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
