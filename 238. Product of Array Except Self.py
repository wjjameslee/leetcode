class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        l = len(nums)
        ptr = 1
        for i in range(l):
            output.append(ptr)
            ptr = ptr * nums[i]
        
        ptr = 1
        for i in reversed(range(l)):
            output[i] = output[i] * ptr
            ptr = ptr * nums[i]
        return output
                