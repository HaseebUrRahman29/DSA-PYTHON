# #MATRIX/2D LIST PRACTICE
# #UPPER TRIANGLE
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# row=len(nums)
# clm=len(nums[0])
# for i in range(0,row):
#     for j in range(0,clm):
#         if j>=i:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()


# #LOWER TRIANGLE
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# row=len(nums)
# clm=len(nums[0])
# for i in range(0,row):
#     for j in range(0,clm):
#         if j<=i:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()



# #DIAGONAL
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# row=len(nums)
# clm=len(nums[0])
# for i in range(0,row):
#     for j in range(0,clm):
#         if j==i:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()



# #OPPOSITE DIAGONAL
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# n=len(nums)
# row=len(nums)
# clm=len(nums[0])
# for i in range(0,row):
#     for j in range(0,clm):
#         if i+j==n-1:
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()


# #TRANSPOSE OF MATRIX
# nums=[[5,9,1],[2,3,7]]
# row=len(nums)
# clm=len(nums[0])
# result=[[0]*row for _ in range(clm)]
# for i in range(row):
#     for j in range(clm):
#         result[j][i]=nums[i][j]
# print(result)