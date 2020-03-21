class Solution:
    def reverse(self, x: int) -> int:
        import math
        neg = False
        if x == 0:
            return 0
        if x < 0:
            x = -x
            neg = True
        e = math.floor(math.log10(x))
        value = 0
        i = 0
        while x:
            r = x % 10
            x = x // 10
            
            toAdd = int(r * math.pow(10, e-i))
            
            if (value + toAdd) >= int(math.pow(2,31)-1):
                return 0
            value += toAdd
            i += 1
        if neg:
            return value * -1
        return value
           