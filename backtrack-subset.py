from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(start,ans):
            
            if start==n:
                res.append(ans[:])#add the current subset upon end of recursion
                return
            #does not need this requirement:if ans not in res, , beacuse there would be no duplicate 
                
            backtrack(start+1,ans)
            
            ans.append(nums[start])
            backtrack(start+1,ans)
            ans.pop()
        backtrack(0,[])
        return res

    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)