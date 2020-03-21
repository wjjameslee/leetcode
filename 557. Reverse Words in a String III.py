class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reverse_words = []
        for word in words:
            reverse_words.append(word[::-1])
        return " ".join(reverse_words)
            