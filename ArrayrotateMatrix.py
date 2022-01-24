from typing import List

#1886. Determine Whether Matrix Can Be Obtained By Rotation
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        #An easy way to Rotate a matrix once by 90 degrees clockwise, 
        # transpose:  flips a matrix over its diagonal, then
        # reflect: interchange the 'j'th and 'n-1-j'th column, for 0<=j<=n-1 where n is the number of columns in matrix.
        for i in range(4):
            if mat==target:return True
            mat=[list(i) for i in zip(*mat[::-1])] #O(n^2)
            #print(mat)
        return False
        #to zip a matrix is to transpose it. 
        #to rotate, zip first then reverse column, is to interchange column 'j'th and 'n-1-j'th
        #reverse rows first, then transpose == zip.
        """
        the zip function itself runs in O(1) time, as it just allocates a special iterable 
        (called the zip object), and assigns the parameter array to an internal field. 
        The function invocation itself (before control reaches in zip) is O(N), 
        as the interpreter must convert the parameters to an array. 
        Every subsequent next call on the iterator also runs in O(N). 
        Exhausting the zip object is therefore O(N*M) 
        assuming M is the average (or minimum) length of the iterables, 
        excluding the time the iterables themselves take to generate items
         (as it is independent of zip)."""

#48. Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #transpose then reflect
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]