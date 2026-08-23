#LARGEST ELEMENT IN AN ARRAY
nums=[55,32,-97,99,3,67]
largest=0
for i in range (0,len(nums)):
    if nums[i]>largest:
        largest=nums[i]
print(largest)