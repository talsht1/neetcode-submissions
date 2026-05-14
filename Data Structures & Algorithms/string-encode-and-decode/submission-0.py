class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string: str = ""
        for string in strs:
            encoded_string = encoded_string + f"{len(string)}:{string}"  
        return encoded_string

    def decode(self, s: str) -> List[str]:
        out, i = [], 0
        while i < len(s):
            j = s.index(":", i)
            n = int(s[i:j])
            out.append(s[j + 1 : j + 1 + n])
            i = j + 1 + n
        return out
