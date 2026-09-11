class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        index = 0
        for num in nums:
            if num in numDict:
                return([numDict[num],index])
            numDict[(target-num)] = index
            index = index + 1
        