class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        sample = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    sample.append([i,j])
        print(sample)
        for x in sample:
            i,j = x
            print(i,j)
            for k in range(m):
                matrix[k][j]=0
            for k in range(n):
                matrix[i][k]=0
            
        