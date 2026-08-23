class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)},"
        encoded += "||"
        encoded += "".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        lens,words = s.split("||")
        lens = lens.split(",")
        decoded = []
        pointer = 0
        for length in lens:
            if length =='':
                continue
            decoded.append(words[pointer:pointer+int(length)])
            pointer = pointer + int(length)
        return decoded
