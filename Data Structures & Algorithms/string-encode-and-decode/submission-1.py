class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "éé"
        return "é".join(strs)

    def decode(self, s: str) -> List[str]:
        if (s == "éé"):
            return []
        return s.split("é")
