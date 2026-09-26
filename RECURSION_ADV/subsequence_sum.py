#GENERATE SUBSEQUENCES WITH SUM K
nums=[5,9,4]
target=9
result=[]
def solve(index,total,subset):
    if total==target:
        result.append(subset.copy())
        return
    elif index>=len(nums):
        return
    elif total>target:
        return
    subset.append(nums[index])
    total=total+nums[index]
    solve(index+1,total,subset)
    e=subset.pop()
    total=total-e
    solve(index+1,total,subset)

solve(0,0,[])
print(result)