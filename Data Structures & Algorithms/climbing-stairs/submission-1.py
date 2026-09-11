class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n

        prev, curr  = 2 , 3

        for i in range(4, n + 1):
            temp = prev + curr
            prev = curr
            curr = temp
        return curr