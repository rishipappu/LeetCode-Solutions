class Solution:
    def finalString(self, s: str) -> str:
        bugged = ""
        s = list(s)
        for i in s:
            if i == "i":
                bugged = bugged[::-1]
            else:
                bugged += i
        return bugged
