class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        curr = (min(heights[l],heights[r])) * (abs(l - r))
        greatest = curr

        while (l != r):
            print(l,r,curr,greatest)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

            curr = (min(heights[l],heights[r])) * abs((l - r))
            if greatest < curr:
                greatest = curr
        
        return(greatest)
            
        