#SET MATRIX ZERO(LEETCODE 73)
nums=[[7,10,29,3],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
row=len(nums)
clm=len(nums[0])
row_trck=[0]*row #[0 for _ in range(row)]
clm_trck=[0]*clm
for i in range(row):
    for j in range(clm):
        if nums[i][j]==0:
            row_trck[i]=-1
            clm_trck[j]=-1
for i in range(row):
    for j in range(clm):
        if row_trck[i]==-1 or clm_trck[j]==-1:
            nums[i][j]=0 
print(nums)