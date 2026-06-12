class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in result:
                return [result[difference], i]
            else:
                result[nums[i]] = i 
        


