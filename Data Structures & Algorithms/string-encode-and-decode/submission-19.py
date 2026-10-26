class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for w in strs:
            res += f"{len(w)}#{w}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1
            
            i += 1
            length = int(length)

            res.append(s[i:i + length])
            i += length
        
        return res