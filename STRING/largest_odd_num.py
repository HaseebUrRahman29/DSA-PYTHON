#LARGEST ODD NUMBER IN STRING(1903)
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n=len(num)
        count=-1
        for i in range(0,n):
            if int(num[i])%2!=0:
                count=i
        if count==-1:
            return ""
            
        odd=num[:count+1]
        return odd