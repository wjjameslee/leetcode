class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        no_dashes = S.replace("-", "")
        remaining_groups = len(no_dashes) // K
        remaining_letters = len(no_dashes) % K
        result_str = ""
        letters_so_far, i = 0, 0
        if remaining_letters != 0:
            i = remaining_letters
            result_str += no_dashes[:i] + "-"
        if remaining_groups == 0:
            result_str = result_str[:-1]
        while remaining_groups:
            letters_so_far = 0
            while letters_so_far < K:
                result_str += no_dashes[i]
                i += 1
                letters_so_far += 1
            
            if remaining_groups != 1:
                result_str += "-"
            remaining_groups -= 1
        return result_str.upper()