class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # For this problem, a linear solution with constant space exists:
        # Take two baskets (as variables), update the # of items in each basket
        # (blen1, blen2) and the consecutive # of items (b1con, b2con) as we go
        # Idea: Encountering a third number not in basket 1 or basket 2, swap
        #       basket 2 to basket 1 and assign basket 2 as this third number
        # Make sure to take care of the three edge cases:
        # 1. When basket 1 or basket 2 are empty
        # 2. When there are at most 2 distinct elements in the given tree
        # 3. When an unseen 3rd number is discovered and the number before it
        #    is in basket 1
        maxtotal = 0
        L = len(tree)
        b1, b2 = -1, -1
        blen1, blen2, b1con, b2con = 0, 0, 0, 0
        for i in range(L):
            if tree[i] == b1:
                blen1 += 1
                if tree[i-1] == b1:
                    b1con += 1
                else:
                    b1con = 1
                continue
            elif tree[i] == b2:
                blen2 += 1
                if tree[i-1] == b2:
                    b2con += 1
                else:
                    b2con = 1
                continue
            if b1 == -1:
                b1 = tree[i]
                b1con += 1
                blen1 += 1
                continue
            elif b2 == -1:
                b2con += 1
                b2 = tree[i]
                blen2 += 1
                continue
            
            if tree[i] != b1 and tree[i] != b2:
                maxtotal = maxtotal if maxtotal >= (blen1 + blen2) else (blen1 + blen2)
                if b2 != tree[i-1]:
                    blen1 = b1con
                else:
                    b1 = b2
                    blen1 = b2con
                b2 = tree[i]
                b2con, blen2 = 1, 1
        # at most 2 distinct numbers; can be only 1 too eg. [1, 1, 1]
        res = maxtotal = maxtotal if maxtotal >= (blen1 + blen2) else (blen1 + blen2)
        return res
            