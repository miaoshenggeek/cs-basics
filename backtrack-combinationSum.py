from typing import List

#https://leetcode.com/problems/combination-sum/solution/
class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def backtrack(start,remain,ans): #remain is sum to fulfill
            if remain==0:
                res.append(ans[:]) #deep copy list(ans)/ans[:]
                return
            elif remain<0:
                return
            
            for i in range(start,len(can)):
                ans.append(can[i])
                backtrack(i,remain-can[i],ans) # give the current number another chance, rather than moving on
                ans.pop()
                #At the end of each exploration, we backtrack by popping out the candidate out of the combination.
            #without for loop
            '''
            backtrack(start+1,remain,ans)
            ans.append(can[start])
            backtrack(start,remain-can[start],ans)
            ans.pop()
            '''
        backtrack(0,target,[])
        return res
    #Let N be the number of candidates, T be the target value, 
    # and M be the minimal value among the candidates.
    #Time O(N^(T/M +1))the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree. 
    # The total number of steps during the backtracking would be the number of nodes in the tree.
    #we can say that the time complexity is linear to the number of nodes of the execution tree.
    #Space O(T/M)