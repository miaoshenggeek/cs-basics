

class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]

#using 2 stacks,time O(|s|),space(|digit|+|alpha|) #394
class Solution(object):
    def decodeString(self, s):
        S=[]
        N=[]
        curstring=""
        k=0
        for i in s:
            if i.isdigit():
                k=k*10+int(i)
            elif i.isalpha():
                curstring+=i
            elif i=='[':
                S.append(curstring)
                N.append(k)
                curstring=""
                k=0
            else:
                print(S)
                curk=N.pop()
                prev=S.pop()
                curstring=prev+curk*curstring
                #print(curstring)
        return curstring

"""
Example: "3[a2[c]]"
Iterate to find the position of the matching close bracket for an open bracket, let name it closePos.
In the above example: closePos[1] = 7, closePos[4] = 6.
Build a dfs(l, r) function to return decoded string from index left l to r (inclusive):
Iterate from i in range [l..r]
If s[i] is digit then num = num * 10 + int(s[i])
Else if s[i] == [ then ans += num * dfs(i + 1, closePos[i] - 1)
Else ans += s[i]
Return dfs(0, len(s) - 1)."""
#Time: O(M), where M is the size of the output answer.
#Space: O(M)
class Solution:
    def decodeString(self, s: str) -> str:
        closePos = {}
        st = []
        for i, c in enumerate(s):
            if c == '[':
                st.append(i)
            elif c == ']':
                closePos[st.pop()] = i

        def solve(l, r):
            num = 0
            ans = []
            while l <= r:
                c = s[l]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    ans.append(num * solve(l + 1, closePos[l] - 1))
                    num = 0
                    l = closePos[l]
                else:
                    ans.append(c)
                l += 1
            return "".join(ans)

        return solve(0, len(s) - 1)