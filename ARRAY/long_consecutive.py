# #LONGEST CONSECUTIVE SEQUENCE
# nums=[1,99,101,98,2,5,3,100,1,1]
# nums.sort()
# n=len(nums)
# count=1
# max_count=1
# for i in range(0,n-1):
#     if nums[i]==nums[i+1] or nums[i+1]-nums[i]!=1:
#         count=1
#     if nums[i+1]-nums[i]==1:
#         count+=1
#         max_count=max(max_count,count)
# print(max_count)


#OPTIMAL
nums=[1,99,101,98,2,5,3,100,1,1]
nums_set=set(nums)
max_count=0
for i in nums_set:
    if i-1 not in nums_set:
        count=1
        while i+count in nums_set:
            count+=1
        max_count=max(max_count,count)
print(max_count)