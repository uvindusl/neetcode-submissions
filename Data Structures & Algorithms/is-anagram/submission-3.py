class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        for i in s:
            list.append(i)
        
        if len(s) != len(t):
            return False
        
        for j in t:
            if j in list:
                list.remove(j)
        
        if len(list) == 0:
            return True
        else:
            return False


