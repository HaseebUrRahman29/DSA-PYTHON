#CHECK WETHER A ARRAY IS SORTED OR NOT
nums=[3,5,6,7,9,10]
sorted_array=True
for i in range(0,len(nums)-1):
    if nums[i]>nums[i+1]:
        sorted_array=False
        break    

print(sorted_array)