class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):          # till last element 
            for j in range(i + 1, len(nums)):   # starting from 2 element 
                if nums[i] + nums[j] == target:
                    return [i,j]