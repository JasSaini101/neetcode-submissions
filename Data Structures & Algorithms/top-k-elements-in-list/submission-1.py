class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numDict = defaultdict(int)
        curr = 1

        for num in nums:
            numDict.update({str(num): (numDict[str(num)] + 1)})
            curr = num

        ans = []
        while k > 0:
            greatest = 0
            for num in numDict:
                print(num, numDict[num])
                if numDict[num] > greatest:
                    greatest = numDict[num]
                    curr = num
            ans.append(curr)
            numDict.pop(curr)
            k -= 1

        return(ans)