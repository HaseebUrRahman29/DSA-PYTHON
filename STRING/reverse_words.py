#REVERSE WORDS IN A STRING(151)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        words=s.split()
        words.reverse()
        result=" ".join(words)
        
        
        return result