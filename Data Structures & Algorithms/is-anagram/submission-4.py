class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list = list(s) 

        if len(s) != len(t):
            return False
        
        for j in t:
            if j in char_list :
                char_list .remove(j)
        
        if len(char_list ) == 0:
            return True
        else:
            return False



