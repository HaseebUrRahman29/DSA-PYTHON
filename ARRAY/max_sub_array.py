# #MAXIMUM SUB ARRAY SUM(brute force)
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# max=float("-inf")
# n=len(nums)
# total=0
# for i in range(0,n):
#     total=0
#     for j in range(i,n):
#         total+=nums[j]
#         if max<total:
#             max=total
# print(max)


#OPTIMAL
nums=[-2,1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
n=len(nums)
total=0
for i in range(0,n):
    total+=nums[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
print(maxi)