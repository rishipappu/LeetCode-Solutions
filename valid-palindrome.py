import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = re.sub(r"[\W_]", "", s).lower()
        return palindrome == palindrome[::-1]
