class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        L = len(s)
        occurrences = {}
        for c in s:
            if c not in occurrences:
                occurrences[c] = 1
            else:
                occurrences[c] += 1
        
        if L % 2 == 0:
            for k, v in occurrences.items():
                if v % 2 == 1:
                    return False
            return True
        else:
            count_odd_occs, count_even_occs = 0, 0
            for k, v in occurrences.items():
                if v % 2 == 1:
                    count_odd_occs += 1
                else:
                    count_even_occs += 1
            if count_odd_occs != 1:
                return False
            num_items = len(occurrences)
            if count_even_occs != num_items - 1:
                return False
            return True
            
            
        