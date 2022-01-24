from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        a=shift[0][0]
        b=shift[0][1]
        for i,j in shift[1:]:
            if a==i:b+=j
            else:b-=j
        if b==0:return s
        if b<0: 
            a=1-a
            b=-b
        if b>len(s):
            b=b%len(s)
        #print(a,b)
        if a==0:
            return s[b:]+s[:b]
            #A left shift by 1 means remove the first character of s and append it to the end.
        else:
            return s[-b:]+s[:-b]
            #a right shift by 1 means remove the last character of s and add it to the beginning.
        