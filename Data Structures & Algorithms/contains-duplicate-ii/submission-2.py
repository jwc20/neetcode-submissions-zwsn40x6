from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l= 0
        while l < len(nums) - 1:
            for r in range(l+1, len(nums)):
                if nums[l] == nums[r]:
                    if abs(l - r) <= k:
                        return True
            l += 1
        return False