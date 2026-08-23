#REMOVE DUPLICTES FROM A SORTED ARRAY
# BRUTE FORCE
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
new_dict={}
for i in range(0,len(nums)):
    if nums[i] in new_dict:
        new_dict[nums[i]]=0
    else:
        new_dict[nums[i]]=0
j=0
for k in new_dict:
    nums[j]=k
    j+=1
print(j)


#OPTIMAL WAY
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
n=len(nums)
if n==1:
    print(n)
i=0
j=i+1
while j<n:
    if nums[j]!=nums[i]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(i+1)