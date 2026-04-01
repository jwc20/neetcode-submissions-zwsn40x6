from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l= 0
        for l in range(len(nums)):
            for r in range(l+1, min(len(nums), l + k + 1)):
                if nums[l] == nums[r]:
                    if abs(l - r) <= k:
                        return True
            l += 1
        return False