class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {} 
        unvisited = set()
        for i in range(n):
            unvisited.add(i)

        #create the graph:
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
            

        cc = 0
        def dfs(u, parent):
            if parent != -1:
                unvisited.remove(u)

            for v in graph.get(u, []):
                if v == parent or v not in unvisited:
                    continue
                else: 
                    dfs(v, u)
        
        while unvisited:
            curr = unvisited.pop()
            dfs(curr, -1)
            cc += 1
        
        return cc
            
        