#MAXIMUM DEPTH OF PARENTHESIS
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_dept=0
        cur_dept=0
        for i in s:
            if i=="(":
                cur_dept+=1
                max_dept=max(max_dept,cur_dept)
            elif i==")":
                cur_dept-=1
        return max_dept

#TC=O(n)
#SC=O(d)