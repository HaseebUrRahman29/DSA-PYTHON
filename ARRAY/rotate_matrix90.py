#LEETCODE 48
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        clm=len(matrix[0])
        n=len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        #TC=O(n^2)
        #SC=O(1)