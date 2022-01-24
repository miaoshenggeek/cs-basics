from typing import List

#let's only add them when we know it will remain a valid sequence. 
# We can do this by keeping track of the number of opening and closing brackets we have placed so far.
# We can start an opening bracket if we still have one (of n) left to place. 
# And we can start a closing bracket if it would not exceed the number of opening brackets.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
    #Time Complexity : O(4^n/n^0.5) Each valid sequence has at most n steps during the backtracking procedure.
    #space same as time