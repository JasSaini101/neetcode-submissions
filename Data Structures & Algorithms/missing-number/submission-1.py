class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total, maxTotal = 0, len(nums)
        for index, num in enumerate(nums):
            total += num
            maxTotal += index

        print(total, maxTotal)
        return(maxTotal - total)