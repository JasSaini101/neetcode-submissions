class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = dict()
        t_letters = dict()
        for letter in s:
            try:
                s_letters[letter] = s_letters[letter] + "1"
            except:
                s_letters[letter] = "1"
        for letter in t:
            try:
                t_letters[letter] = t_letters[letter] + "1"
            except:
                t_letters[letter] = "1"
        if(s_letters == t_letters):
            return True
        return False