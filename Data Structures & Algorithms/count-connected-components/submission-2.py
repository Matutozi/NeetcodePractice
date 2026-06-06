class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_l = {i:[] for i in range(n)}

        for a,b in edges:
            adj_l[a].append(b)
            adj_l[b].append(a)

        visited = set()

        component = 0

        for num in range(n):
            if num in visited:
                continue

            component += 1

            stack = [num]

            while stack:
                node = stack.pop()

                if node in visited:
                    continue
                visited.add(node)

                for nei in adj_l[node]:
                    if nei not in visited:
                        stack.append(nei)
        return component
