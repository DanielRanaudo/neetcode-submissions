class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #key is node, val is list:
        graph = {} 

        #create the graph
        for pair in prerequisites:
            pre = pair[1]
            if pre not in graph:
                graph[pre] = [pair[0]]
            else: graph[pre].append(pair[0])

        

        #now we have a full graph, we want to make sure there are no cycles,
        #this can be done through dfs/bfs, tracking visited
        
        def dfs(u, visited, safe):
            visited.add(u)
                
            for v in graph.get(u, []):
                if v in visited:
                    return False
                if v not in safe:
                    if not dfs(v, visited, safe):
                        return False

            visited.remove(u)
            safe.add(u)

            return True

        visited = set()
        safe = set()
        for course in range(numCourses):
            if course not in safe:
                if not dfs(course, visited, safe):
                    return False
            
        return True




        