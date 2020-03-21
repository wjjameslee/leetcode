class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        global_max = float('-inf')
        local_max = 0
        for i in range(l):
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > global_max:
                global_max = local_max
            
        return global_max