class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = dict()
        dic2 = dict()

        for char in s:
            if char not in dic1:
                dic1[char] = 0
            dic1[char] += 1
        
        for char in t:
            if char not in dic2:
                dic2[char] = 0
            dic2[char] += 1

        if dic1 != dic2:
            return False
        return True