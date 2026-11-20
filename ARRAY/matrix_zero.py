#SET MATRIX ZERO(LEETCODE 73)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        clm=len(matrix[0])
        row_trk=[0]*row
        clm_trk=[0]*clm
        for i in range(row):
            for j in range(clm):
                if matrix[i][j]==0:
                    row_trk[i]=-1
                    clm_trk[j]=-1
        for i in range(row):
            for j in range(clm):
                if row_trk[i]==-1 or clm_trk[j]==-1:
                    matrix[i][j]=0

        #TC=O(n*m)
        #SC=O(n+m)