class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for j in t:
            if j in s:
                s = s.replace(j, "", 1)
            else:
                return False
        
        return True



