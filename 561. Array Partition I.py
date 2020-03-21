class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array and create pairs by iterating index from first and last entry, until they converge
        nums.sort()
        # eg. [1, 4, 3, 2] -> [1, 2, 3, 4] (Add up every even index from i = 0 since min(A[i], A[i+1]) will be A[i])
        return sum(nums[::2])