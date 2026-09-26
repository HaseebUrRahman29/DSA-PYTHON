#CHECK SUBSEQUENCES WITH SUM K
nums=[5,9,4]
target=9
result=[]
def solve(index,total,subset):
    if total==target:
        result.append(subset.copy())
        return True
    elif index>=len(nums):
        return False
    elif total>target:
        return False
    subset.append(nums[index])
    total=total+nums[index]
    pick=solve(index+1,total,subset)
    if pick==True:
        return True
    e=subset.pop()
    total=total-e
    not_pick=solve(index+1,total,subset)
    if not_pick==True:
        return True
    return False

solve(0,0,[])
print(result)