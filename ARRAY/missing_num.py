#FIND MISSING NUMBERS IN A ARRAY
nums=[9,6,4,2,3,5,7,0,1]
n=len(nums)
sum=n*(n+1)//2
total=0
for i in nums:
    total+=i
print(sum-total)