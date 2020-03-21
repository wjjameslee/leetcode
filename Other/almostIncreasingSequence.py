'''Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence 
by removing no more than one element from the array.
Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
Sequence containing only one element is also considered to be strictly increasing.
'''

def almostIncreasingSequence(sequence):
    slen = len(sequence)
    threshold, threshold2 = 0, 0
    for i in range(slen - 1):
        if sequence[i] >= sequence[i + 1]:
            threshold += 1
    for i in range(slen - 2):
        if sequence[i] >= sequence[i + 2]:
            threshold2 += 1
    if threshold > 1:
        return False
    if threshold2 > 1:
        return False
    return True


