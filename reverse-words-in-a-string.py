class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [word for word in words if word != ""]
        words = " ".join(words[::-1])
        return words
