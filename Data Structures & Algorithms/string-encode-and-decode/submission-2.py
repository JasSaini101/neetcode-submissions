class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + s + "xXx"
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded, index = [], s.index("xXx")
        
        while(s):
            index = s.index("xXx")
            decoded.append(s[0:index])
            s = s[index+3:]
        return decoded