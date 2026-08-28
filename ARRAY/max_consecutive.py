#MAX CONSECUTIVE ONES
nums=[1,1,0,1,0,1,1,1,1,0,1,1,1,1,1]
count=0
max_count=0
n=len(nums)
for i in range(0,n):
    if nums[i]==1:
        count+=1
        if count>max_count:
            max_count=count
    else:
        count=0
print(max_count)