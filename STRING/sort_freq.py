#SORT CHARACTERS BY FREQUENCY
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sort_chr=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for ch,i in sort_chr:
            result+=ch*i
        return result
        
#TC=O(nlogn)
#SC=O(n)