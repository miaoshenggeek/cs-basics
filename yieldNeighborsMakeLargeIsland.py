from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        
        #generator
        #generator comprehension
        # csv_gen = (row for row in open(file_name))
        # alternative: def csv_reader(file_name):
        #                  for row in open(file_name, "r"):
        #                        yield row
        def neighbors(r, c): #equal to iterator 
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc
                    
        def dfs(grid,i,j,idx):
            nonlocal ans
            if i<0 or i>=len(grid) or j<0 or j>=len(grid) or not grid[i][j]==1:
                return
            ans+=1
            grid[i][j]=idx
            dfs(grid,i-1,j,idx)
            dfs(grid,i+1,j,idx)
            dfs(grid,i,j-1,idx)
            dfs(grid,i,j+1,idx)
            
        rt={0:0}
        idx=2
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ans=0
                    dfs(grid,i,j,idx)
                    rt[idx]=ans
                idx+=1
        ans=max(rt.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    #how to use generator
                    candidate={grid[nr][nc] for nr,nc in neighbors(i,j) if grid[nr][nc]>1}
                    ans=max(ans,1+sum(rt[i] for i in candidate))
                      
        return ans


        #alternative dfs using 4-neighbors
        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            #how to use generator
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans
        #to call dfs
        if grid[r][c] == 1:
            area[index] = dfs(r, c, index)
            index += 1
        

    
        
            
            
    
        