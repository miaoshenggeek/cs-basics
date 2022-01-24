class Solution:
    #408
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        s1=s2=0
        while s1<len(word) and s2<len(abbr):
            num=""
            while s2<len(abbr) and abbr[s2].isdigit():
                num+=abbr[s2]
                s2+=1
            #print("A"+num)
            if num.startswith("0"):return False
            if num:s1+=int(num)
            
            if s1<len(word) and s2<len(abbr) :
                if word[s1]==abbr[s2]:
                    s1+=1
                    s2+=1
                else:
                    return False
        #print(s1,s2)
        return s1==len(word) and s2==len(abbr)
    '''
    "internationalization"
    "i12iz4n"
    "apple"
    "a2e"
    "a"
    "01"
    "internationalization"
    "i5a11o1"
    '''
            