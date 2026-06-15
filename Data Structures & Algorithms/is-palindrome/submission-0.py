class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCasedInput = "".join(filter(str.isalnum, s.lower()))
        left = 0
        right = len(lowerCasedInput) - 1
        while (left < right):
            if(lowerCasedInput[left] != lowerCasedInput[right]):
                return False
            left += 1
            right -= 1
        

        return True
