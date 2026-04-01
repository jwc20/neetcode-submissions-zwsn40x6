class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        l, r = 0, 1
        while r < len(nums):
            if abs(nums[l] - nums[r]) == 0:
                return True
            l, r = r, r+1

        return False
         