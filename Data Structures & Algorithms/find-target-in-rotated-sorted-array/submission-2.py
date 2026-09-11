class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mp = len(nums) // 2
        index = 0
        
        while(mp):
            if(nums[0] <= nums[mp]):
                if(nums[0] <= target and nums[mp] > target):
                    nums = nums[0:mp]
                else:
                    nums = nums[mp:]
                    index += mp
            else:
                if(nums[0] > target and nums[mp] > target or nums[0] == target):
                    nums = nums[0:mp]
                else:
                    nums = nums[mp:]
                    index += mp
            mp = len(nums) // 2

        if nums[0] == target:
            return(index)
        return(-1)
        


        