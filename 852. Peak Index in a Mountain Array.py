class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # Bruteforce: Keep track of which index is the most recent before A[lt_index] < A[lt_index + 1] fails; O(n)
        # Divide and Conquer: Start from the middle; stop when low and high converges; O(logn)
        low = 0
        high = len(A) - 1
        while low < high:
            mid = (low+high) // 2
            # Since mid is always less high; eg. [1, 4], low = 0, high = 1; mid ~= 0
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low
                