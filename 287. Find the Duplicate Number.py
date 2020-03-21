class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = nums[0], nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        ptr1, ptr2 = nums[0], tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
