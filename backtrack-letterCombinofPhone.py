from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]: #"23"
        dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        #digits=digits.replace("1","")
        if not digits:return
        n=len(digits)
        res=[]
        
        def backtrack(start,ans):
            if len(ans)==n:
                res.append("".join(ans))
                return
            if start==n:
                return
            for i in dic[digits[start]]:
                ans.append(i)
                backtrack(start+1,ans)
                ans.pop()
        backtrack(0,[])
        return res
        #Time complexity: O(4^N * N) where N is the length of digits. 
        # Note that 4 in this expression is referring to
        # the maximum value length in the hash map
        #space: O(N)space occupied by the recursion call stack. 
        # It will only go as deep as the number of digits in the input 
        # since whenever we reach that depth, we backtrack.