#COMBINATION SUM 2
class Solution(object):
    def solve(self,index,total,subset,candidates,target,result):
        if total==0:
            result.append(subset[:])
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>total:
                break
            
            subset.append(candidates[i])
            self.solve(i+1,total-candidates[i],subset,candidates,target,result)
            subset.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        self.solve(0,target,[],candidates,target,result)
        return result