from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        # Do a DFS to find all cells in the current island.
        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            path_signature.append(direction)
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            path_signature.append("0") #get the path of backtracking
        
        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path_signature = []
                dfs(row, col, "0")
                if path_signature:
                    unique_islands.add(tuple(path_signature))
        
        return len(unique_islands)
#calculate a hash for each island 
# in such a way that ensured two identical islands have the same hash value. 
#In Python, there is a data structure called a frozenset that we have to use instead,
#Python doesn't allow inserting a set into another set. A frozenset is an immutable set.
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        # Do a DFS to find all cells in the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if current_island:
                    unique_islands.add(frozenset(current_island)) #tuple and frozenset are hashable
        
        return len(unique_islands)