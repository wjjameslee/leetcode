class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        # Divide and Conquer: T(n) = 2T(n/2) + 2O(n) => O(nlogn)
        def majorityCheck(lo, hi):
            if lo == hi:
                return nums[lo]
            
            mid = (lo + hi) // 2
            left_majority = majorityCheck(lo, mid)
            right_majority = majorityCheck(mid+1, hi)
            
            if left_majority == right_majority:
                return left_majority
            else:
                left_count, right_count = 0, 0
                for elem in nums[lo:mid+1]:
                    if elem == left_majority:
                        left_count += 1
                for elem in nums[mid+1:hi+1]:
                    if elem == right_majority:
                        right_count += 1
                if right_count == left_count:
                    return right_majority
                return right_majority if right_count > left_count else left_majority
        
        
        # return majorityCheck(0, len(nums) - 1)
        '''
        count = 0
        candidate = None
        for elem in nums:
            if count == 0:
                candidate = elem
                count += 1
            elif candidate == elem:
                count += 1
            else:
                count -= 1
        return candidate