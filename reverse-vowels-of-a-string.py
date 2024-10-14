class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        vowels = ["a", "e", "i", "o", "u"]
        reversevowels = []
        for letter in range(len(letters)):
            if letters[letter].lower() in vowels:
                reversevowels.append(letters[letter])
                letters[letter] = ""

        reversevowels = reversevowels[::-1]
        reverse = ""
        currentvowel = 0
        for i in letters:
            if i == "":
                reverse += reversevowels[currentvowel]
                currentvowel += 1
            else:
                reverse += i
        return reverse
