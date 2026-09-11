#REMOVE OUTERMOST PARENTHESES(1021)
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        count=0
        for ch in s:
            if ch=="(":
                count+=1
                if count>1:
                    result+=ch
            else:
                count-=1
                if count>0:
                    result+=ch
        return result