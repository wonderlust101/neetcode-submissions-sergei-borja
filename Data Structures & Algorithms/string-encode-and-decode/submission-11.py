class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        idx = 0

        while idx < len(s):
            length_str = ""

            while s[idx] != "#":
                length_str += s[idx]
                idx += 1
            
            idx += 1
            length = int(length_str)

            res.append(s[idx:idx + length])
            idx += length
        
        return res

        