class Solution:
    def countBits(self, n: int) -> List[int]:
        i, res = 0, []



        for i in range(0,n+1):
            j, count = i, 0
            while(j > 0):
                count += j & 1
                j >>= 1
            res.append((count))
        return(res)



        