#COUNT ALL SUBSEQUENCES WITH SUM K
nums=[5,9,4]
target=9
def solve(index,total):
    if total==target:
        return 1
    elif index>=len(nums):
        return 0
    elif total>target:
        return 0
    pick=solve(index+1,total+nums[index])
    not_pick=solve(index+1,total)
    return pick+not_pick

print(solve(0,0))