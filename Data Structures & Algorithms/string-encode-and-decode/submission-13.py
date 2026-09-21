class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            lenStr = ""

            while s[i] != "#":
                lenStr += s[i]
                i += 1
            
            length = int(lenStr)
            i += 1

            res.append(s[i:i+length])
            i += length
        
        return res