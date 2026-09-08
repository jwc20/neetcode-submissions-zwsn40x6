class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [-1,0,2,4,6,8]
         l    m     r         target = 4 > 2 = nums[mid]
                l m r         target = 4 < 6 = nums[mid]
               l,m r          target = 4 = 4 = nums[mid]
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
