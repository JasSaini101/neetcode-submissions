class Solution:
    def hammingWeight(self, n: int) -> int:
        index, total = 0, 0
        while(n):
            digit = n % 2
            n = n // 2
            if(digit & 1):
                total += 1
        return total