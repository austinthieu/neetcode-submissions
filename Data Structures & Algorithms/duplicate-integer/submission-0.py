class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         result = {}
         for i in range(0, len(nums)):
            if nums[i] in result:
                return True
            result[nums[i]] = 1
         return False
         
        

