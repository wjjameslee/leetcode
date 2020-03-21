class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = []
        le = len(nums)
        nums.sort()
        if le < 3:
            return solution_set
        else:
            for i in range(le-1):
                if i != 0:
                    if nums[i] == nums[i-1]:
                        continue
                j = i + 1
                k = le - 1
                while j < k:
                    sums = nums[i] + nums[j] + nums[k]
                    if sums == 0:
                        solution_set.append([nums[i], nums[j], nums[k]])
                        jval, kval = nums[j], nums[k]
                        while j < k and nums[j] == jval: j += 1
                        while j < k and nums[k] == kval: k -= 1
                    elif sums > 0:
                        k -= 1
                    else:
                        j += 1
                
        return solution_set
    
                        
                
                        