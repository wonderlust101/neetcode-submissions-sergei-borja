class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        pos = 0
        res = []

        while pos != len(s):
            temp = ""
            while s[pos] != "#":
                temp += s[pos]
                pos += 1
            
            str_len = int(temp)
            pos += 1

            res.append(s[pos:pos + str_len])
            pos += str_len
        
        return res


