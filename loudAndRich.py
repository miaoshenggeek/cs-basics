class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]: 
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)
        #print(graph)
        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return list(map(dfs, range(N)))
        #for i in range(len(quiet)): dfs(i)
        #return res

        """[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]"""