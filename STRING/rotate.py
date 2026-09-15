#ROTATE STRING
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        double_str=s+s
        if goal not in double_str:
            return False
        return True
#TC=O(n)
#SC=O(n)