from typing import Collection, List

#"""[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]"""    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = Collection.defaultdict(dict)#default dict of a dict//
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v
        print(G)
        #defaultdict(<class 'dict'>, {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b': 0.33}})
        #defaultdict(<class 'dict'>, {'a': {'b': 3.4}, 
                                    # 'b': {'a': 0.29411764705882354, 'e': 2.3}, 
                                    # 'e': {'f': 1.4, 'b': 0.4347826086956522}, 
                                    # 'f': {'e': 0.7142857142857143}})
        #//method to put edge weight in Graph//2D-dictionary/2D-matrix
        def bfs(src, dst):
            if not (src in G and dst in G): return -1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst: 
                    return v
                seen.add(x)
                for y in G[x]:
                    if y not in seen: 
                        q.append((y, v*G[x][y]))
            return -1.0
        return [bfs(s, d) for s, d in queries]
        
    """[["a","b"],["c","b"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]"""    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:    
        #//method to use uf to directed edges:no ranks, parent is direction of nodes
        # dict[node]=(parent, weight=node/parent) for edge (node,parent) as (u,v) with weight
        root = {}
	    
        def find(x):
            p, xr = root.setdefault(x, (x, 1.0)) 
            #setdefault used in {} to add {key:default}: if key existed, return the value
            if x != p:
                r, pr = find(p)
                root[x] = (r, xr*pr)#xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
            return root[x]

        # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
        def union(x, y, ratio):
            px, xr = find(x)[0],find(x)[1] #find default if not seen before
            py, yr = find(y)[0],find(y)[1] #find default if not seen before
            if not ratio:
                return xr / yr if px == py else -1.0 #x/r/(y/r)=x/y
            if px != py:
                #  print(root[px])-->print(root[px])
                #  before-->after
                #{'a': ('a', 1.0), 'b': ('b', 1.0)}>>{'a': ('b', 2.0), 'b': ('b', 1.0)}
                #{'a': ('b', 2.0), 'b': ('b', 1.0), 'c': ('c', 1.0)}>>{'a': ('b', 2.0), 'b': ('b', 1.0), 'c': ('b', 3.0)}
                root[px] = (py, yr/xr*ratio) #(y/r)/(x/r)*(x/y)---for new edge, y is root, x befault is 1
                

        for (x, y), v in zip(equations, values):
            union(x, y, v)
        print(root)
        #{'a': ('b', 2.0), 'b': ('c', 3.0), 'c': ('c', 1.0)}

        return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]
        '''
        test for line 51
        [["a","b"],["e","f"],["b","e"]]
        [3.4,1.4,2.3]
        [["b","a"],#["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
        {'a': ('a', 1.0), 'b': ('b', 1.0)}>>{'a': ('b', 3.4), 'b': ('b', 1.0)}
        {'a': ('b', 3.4), 'b': ('b', 1.0), 'e': ('e', 1.0), 'f': ('f', 1.0)}
        {'a': ('b', 3.4), 'b': ('b', 1.0), 'e': ('f', 1.4), 'f': ('f', 1.0)}
        {'a': ('b', 3.4), 'b': ('b', 1.0), 'e': ('f', 1.4), 'f': ('f', 1.0)}
        {'a': ('b', 3.4), 'b': ('f', 3.2199999999999998), 'e': ('f', 1.4), 'f': ('f', 1.0)}

        
        '''

