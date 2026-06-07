class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        string = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1
            
            i += 1 #Skip Hash

            string.append(s[i:i + int(length)])
            i += int(length)
        
        return string