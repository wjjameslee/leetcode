class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        l = len(nums)
        for i in range(l):
            complement = target - nums[i]
            if complement not in ht:
                ht[nums[i]] = i
            else:
                return [ht[complement], i]
        
        