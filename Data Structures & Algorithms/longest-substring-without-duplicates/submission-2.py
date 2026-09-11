class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        currSet = set({})
        i, greatest = 0, 0

        while(i < len(s)):
            prevLen = len(currSet)
            currSet.add(s[i])
            if(prevLen == len(currSet)): #duplicate
                if prevLen > greatest:
                    greatest = prevLen
                index = s.find(s[i])
                s = s[index + 1:]
                i = 0
                currSet = {s[i]}
            i += 1
        
        return(max(greatest, len(currSet)))