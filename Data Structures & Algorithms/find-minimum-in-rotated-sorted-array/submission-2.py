class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        half = len(nums)//2

        while(half):
            if(min(nums[0], nums[half-1]) < min(nums[half], nums[-1])):
                nums = nums[0:half]
            else:
                nums = nums[half:]
            half = len(nums)//2
        return(nums[0])
