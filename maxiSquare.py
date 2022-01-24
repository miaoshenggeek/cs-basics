class Solution:
    def maximalSquare(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
        '''print(A)
        print(list(map(max, A)))
        print(13 and 11)
        print(0 and 11)'''
        # I return 0 for the empty matrix and otherwise the area of the largest square ending anywhere.
        return len(A) and max(map(max, A)) ** 2