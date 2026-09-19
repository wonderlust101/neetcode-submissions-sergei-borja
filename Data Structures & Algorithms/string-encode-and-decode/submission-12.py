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
            str_length = ""

            while s[i] != "#":
                str_length += s[i]
                i += 1
            
            length = int(str_length)
            i += 1

            res.append(s[i : i + length])
            i += length
        
        return res