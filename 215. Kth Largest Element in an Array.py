class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        return nums[N-k]