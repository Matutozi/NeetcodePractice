from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        def dfs(source, target, visited):
            if source == target:
                return True
            visited.add(source)

            for nei in graph[source]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
                        
            return False

        
        for u,v in edges:
            if u in graph and v in graph:
                if dfs(u,v,set()):
                    return [u,v]

            graph[u].append(v)
            graph[v].append(u)
                
        return []