'''Here is the algorithm.
Clean up the input by replacing more than one star in a row by a single star: p = remove_duplicate_stars(p).
Initiate the memoization hashmap dp.
Return the helper function with a cleaned input: helper(s, p).
helper(s, p):
If (s, p) is already known and stored in dp, return the value.
If the strings are equal (p == s), or the pattern matches any string (p == '*'), add dp[(s, p)] = True.
Else if p is empty, or s is empty, add dp[(s, p)] = False.
Else if the current characters match (p[0] == s[0] or p[0] == '?'), 
then compare the next ones and add dp[(s, p)] = helper(s[1:], p[1:]).
Else if the current pattern character is a star (p[0] == '*'), 
then there are two possible situations: the star matches no characters, 
and the star matches one or more characters: dp[(s, p)] = helper(s, p[1:]) or helper(s[1:], p).
Else p[0] != s[0], then add dp[(s, p)] = False.
Now when the value is computed, return it: dp[(s, p)].'''

class Solution:        
    def isMatch(self, s: str, p: str) -> bool:
        #O(p)
        def remove_duplicate_stars(p: str) -> str:
            new_string = []
            for char in p:
                if not new_string or char != '*':
                    new_string.append(char)
                elif new_string[-1] != '*':
                    new_string.append(char)
            return ''.join(new_string)
        #T:O(S*P*(S+P)) S:O(S*P)
        def helper(s: str, p: str) -> bool:
            if (s, p) in dp:
                return dp[(s, p)]
            if p == s or p == '*':
                dp[(s, p)] = True
            elif p == '' or s == '':
                dp[(s, p)] = False
            elif p[0] == s[0] or p[0] == '?':
                dp[(s, p)] = helper(s[1:], p[1:])
            elif p[0] == '*':
                dp[(s, p)] = helper(s, p[1:]) or helper(s[1:], p)
            else:
                dp[(s, p)] = False
                
            return dp[(s, p)]
        
        dp = {}
        p = remove_duplicate_stars(p)        
        return helper(s, p)