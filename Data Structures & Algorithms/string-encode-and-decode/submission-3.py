class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += "#" + str(len(s)) + s

        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        string = ""

        pos = 0

        while pos < len(s):
            if (s[pos] == "#"):
                for l in range(int(s[pos + 1])):
                    string +=s[pos + l + 2]

                res.append(string)
            
            print(res)
            pos += int(s[pos + 1]) + 2
            string = ""

        return res