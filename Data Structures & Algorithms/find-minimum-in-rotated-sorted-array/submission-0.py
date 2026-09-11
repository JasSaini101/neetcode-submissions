class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        index, least = 0 , nums[0]
        while(index < len(nums)):
            if(nums[index] < least):
                least = nums[index]
            index += 1
        return(least)