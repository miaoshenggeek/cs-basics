from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #The letter-logs come before all digit-logs
        letterlog=[]
        digitlog=[]
        for log in logs:
            if log[-1].isdigit():
                digitlog.append(log)
            else:
                letterlog.append(log)
        
        #The letter-logs are sorted lexicographically by their contents then idf.
        letterlog.sort(key=lambda i: (i.split(" ")[1:],i.split(" ")[0]))
        print(letterlog,digitlog)
        return letterlog+digitlog
        # arr1.extend(arr2) return none , only to change arr1
        """
        logs1=[ i for i in logs if i[-1].isalpha() ]
        logs2=[ i for i in logs if i[-1].isdigit() ]
        a=sorted(logs1,key=lambda log: (log.split(" ",1)[1],log.split(" ",1)[0]))
        return a+logs2
        """
        # method string.split(separator, maxsplit) 
        # By default any whitespace is a separator
        # Default maxsplit value is -1, which is "all occurrences"
        # maxsplit 1 means split the first occurred separator