#N-QUEENS
class Solution(object):
    def solve(self,col,n,ans,board,left_row,lower_diagonal,upper_diagonal):
        if col==n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if(
                left_row[row]==0
                and lower_diagonal[row+col]==0
                and upper_diagonal[n-1+col-row]==0):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                left_row[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[n-1+col-row]=1
                self.solve(col+1,n,ans,board,left_row,lower_diagonal,upper_diagonal)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                left_row[row]=0
                lower_diagonal[row+col]=0
                upper_diagonal[n-1+col-row]=0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans=[]
        board=["."*n for _ in range(n)]
        left_row=[0]*n
        lower_diagonal=[0]*(2*n-1)
        upper_diagonal=[0]*(2*n-1)
        self.solve(0,n,ans,board,left_row,lower_diagonal,upper_diagonal)
        return ans