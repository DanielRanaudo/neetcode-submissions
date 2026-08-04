class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        graph = {} 
        visitedEdges = set() #pair of edges to make sure we do not revisit the same
        #we are going to make the edges 
        for pair in edges:
            first = pair[0]
            sec = pair[1]
            if first not in graph:
                graph[first] = [sec]
            else: 
                graph[first].append(sec)
            if sec not in graph:
                graph[sec] = [first]
            else:
                graph[sec].append(first)


        color = [0] * n
        def dfs(u):
            color[u] = 1
            for v in graph[u]:
                if color[v] == 2 or (v, u) in visitedEdges:
                    continue
                visitedEdges.add((u, v))
                if color[v] == 1 or not dfs(v):
                    return False
                
            
            color[u] = 2
            return True
        if len(edges) != n - 1:
            return False
        for u in range(n):
            if not dfs(u):
                return False
        
        return True
            

            
        