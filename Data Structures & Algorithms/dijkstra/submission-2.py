class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        dist = {i: float('inf') for i in range(n)}
        dist[src] = 0
        
        adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
            
        visited = set()
        
        for _ in range(n):
            curr_node = -1
            min_dist = float('inf')
            
            for node in range(n):
                if node not in visited and dist[node] < min_dist:
                    min_dist = dist[node]
                    curr_node = node
            
            if curr_node == -1:
                break
                
            visited.add(curr_node)
            
            for neighbor, weight in adj[curr_node]:
                if dist[curr_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + weight
                    
        for d in dist:
            if dist[d] == float('inf'):
                dist[d] = -1
        return dist