class Solution:
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        words = {word: i for i, word in enumerate(words)}
        result = []
        for word, i in words.items():
            n = len(word)
            for l in range(n+1):
                prefix = word[:l]
                suffix = word[l:]
                if is_palindrome(prefix):
                    match = suffix[::-1]
                    if match != word and match in words:
                        # prepend to current word at index l
                        result.append([words[match], i])
                # Avoid duplicate matches for the empty string suffix, since already used in prefix search
                if l != n and is_palindrome(suffix):
                    # append to current word at index l
                    match = prefix[::-1]
                    if match in words:
                        result.append([i, words[match]])
        return result
            
        