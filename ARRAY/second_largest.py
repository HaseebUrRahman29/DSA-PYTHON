#SECOND LARGEST ELEMENT IN THE LIST
nums=[55,32,97,-55,45,32,88,21]
largest=0
second_largest=0
for i in range(0,len(nums)):
    if nums[i]<largest and nums[i]>second_largest:
        second_largest=nums[i]
    if nums[i]>largest:
        largest=nums[i]
print(second_largest)