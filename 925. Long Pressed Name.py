class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_set, typed_set = set(), set()
        for c in name:
            name_set.add(c)
        for c in typed:
            typed_set.add(c)
        if len(name_set) != len(typed_set):
            return False
        n, t = 0, 0
        tlen, nlen = len(typed), len(name)
        while n < nlen:
            if t == tlen:
                return False
            if typed[t] == name[n]:
                n += 1
                t += 1
            else:
                t += 1
        return True