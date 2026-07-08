class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = 0
        while len(s) != 0:
            if t[count] in s:
                s = s.replace(t[count], "", 1)
            else:
                return False
            count += 1
        return True
        





