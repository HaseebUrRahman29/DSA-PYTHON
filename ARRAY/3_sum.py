# #3SUM PROBLEM(15)
# arr=[-1,0,1,2,-1,-4]
# n=len(arr)
# my_set=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i]+arr[j]+arr[k]==0:
#                 temp=[arr[i],arr[j],arr[k]]
#                 temp.sort()
#                 my_set.add(tuple(temp))

# print(my_set)


#OPTIMAL
from typing import List
class solution:
    def threeSum(self,nums:List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return(ans)
