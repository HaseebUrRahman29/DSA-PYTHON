#ISOMORPHIC STRINGS    
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #PAPER
        if len(s)!=len(t):
            return False
        new_dict={}
        new_dict_rev={}
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]
            if char_s in new_dict:
                if new_dict[char_s]!=char_t:
                    return False
            else:
                new_dict[char_s]=char_t 
            if char_t in new_dict_rev:
                if new_dict_rev[char_t]!=char_s:
                    return False
            else:
                new_dict_rev[char_t]=char_s
        return True

#TC=O(n)
#SC=O(n)