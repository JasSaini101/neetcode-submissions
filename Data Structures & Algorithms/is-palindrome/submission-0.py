class Solution:
    def isPalindrome(self, s: str) -> bool:
        index = 0
        s_AN = ""

        for letter in s:
            if(letter.isalnum()):
                s_AN = s_AN + letter.lower()

        for letter in s_AN:
            if(s_AN[index] != s_AN[-(index+1)]):
                return False
            index = index + 1
        return True
        