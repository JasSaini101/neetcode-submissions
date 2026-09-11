class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i, maxProduct, zeroCount = 0, 1, 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                maxProduct *= num

        if zeroCount > 1:
            return [0] * len(nums)
        
        while(i < len(nums)):
            if zeroCount == 1:
                if nums[i] == 0:
                    nums[i] = maxProduct
                else:
                    nums[i] = 0
            else:
                nums[i] = maxProduct // nums[i]
            i += 1
        
        return(nums)
        