class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        alen = len(nums)
        ptr = 0
        while ptr < alen:
            if nums[ptr] == nums[nums[ptr]-1]:
                ptr += 1
                continue
            elif nums[ptr] != ptr + 1:
                nums[nums[ptr]-1], nums[ptr] = nums[ptr], nums[nums[ptr]-1]
        
        for i in range(alen):
            if nums[i] != i+1:
                result.append(nums[i])
        return result
                