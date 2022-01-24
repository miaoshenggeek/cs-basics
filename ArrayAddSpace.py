from typing import List


def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        n=len(s)
        for i in range(0,n):
            if spaces and i==spaces[0]:
                ans+=" "
                spaces.pop(0)
            ans+=s[i]
        return ans

        """
        alist=[]
        e=0
        for i in range(len(s)):
            if e==len(spaces):
                alist.append(s[i:])
                break
            if i==spaces[e]:
                alist.append(" "+s[i])
                e+=1
                #print(e)
            else:alist.append(s[i])
        return "".join(alist)"""