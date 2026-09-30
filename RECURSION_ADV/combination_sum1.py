#COMBINATION SUM
class Solution(object):
    def solve(self,index,total,subset,candidates,target,result):
        if total==target:
            result.append(list(subset))
            return
        elif total>target:
            return
        elif index>=len(candidates):
            return
        add=total+candidates[index]
        subset.append(candidates[index])
        self.solve(index,add,subset,candidates,target,result)
        add=total
        subset.pop()
        self.solve(index+1,add,subset,candidates,target,result)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result