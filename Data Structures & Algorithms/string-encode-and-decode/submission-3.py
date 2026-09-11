class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += word
            s += '|'
        return s

    def decode(self, s: str) -> List[str]:
        ls = s.split('|')
        ls.pop(-1)
        return ls

