class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Ideas:
        - we want to apply binary search when we are looking through the non-rotated portion of the array
            - where the subarray is strictly increasing
        
        Example:

        [3,4,5,6,1,2], target = 1
         l   m     r     check to see if the elem in the midpoint is greater than the target value
                         if yes, then l = mid + 1
               l m r                       
         
        [1,2,3,4,5,6], target = 2
         l   m     r    right is greater so, r = mid - 1
         l m r

        """

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                l = mid + 1
            else:
                r = mid - 1
            
            if nums[mid] == target:
                return mid
        return -1
