class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = []
        while(n > 0):
            reverse.append(n&1)
            n >>= 1
        
        i, res = 0, 0
        while(i < len(reverse)):
            res += (2**(31-i)) * reverse[i]
            i += 1
        
        return(res)