#TWO SUM PROBLEM
# nums=[5,9,1,2,4,15,6,3]
# n=len(nums)
# target=13
# for i in range(0,n):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             print(i,j)


#OPTIMAL
nums=[5,9,1,2,4,15,6,3]
n=len(nums)
target=13
new_dict={}
for i in range(0,n):
    remaining=target-nums[i]
    if remaining in new_dict:
        print(i,new_dict[remaining])
    new_dict[nums[i]]=i