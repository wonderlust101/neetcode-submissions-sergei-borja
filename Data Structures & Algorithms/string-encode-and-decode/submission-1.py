class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += s + "."

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        string = ""

        for l in s:
            if l != ".":
                string += l
            else:
                res.append(string)
                string += " "
                string = ""

        return res