class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        
        pos = 0
        while pos < len(s):
            length = ""

            while s[pos] != "#":
                length += s[pos]
                pos += 1

            pos += 1

            res.append(s[pos: pos + int(length)])

            pos += int(length)

        return res

