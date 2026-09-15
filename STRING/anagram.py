#VALID ANAGRAM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # anagram
        # nagaram
        if len(s)!=len(t):
            return False
        new_dict={}
        for i in s:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        for i in t:
            if i not in new_dict:
                return False
            else:
                if new_dict[i]==0:
                    return False
                else:
                    new_dict[i]-=1
        return True

#TC=O(n)
#SC=O(1)