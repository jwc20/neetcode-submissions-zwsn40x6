class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        this requires two-pass binary search: first one to find the left and right portions and the second, to find the target in the portion.

        it requires three step.

        1. Find the pivot point, the smallest in the array, to find the left and right portions.
        2. Determine which portion the target is in.
        3. Standard binary search to find the target value in the portion
        """

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 

        pivot = l

        if target >= nums[pivot] and target <= nums[-1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid 

        return -1
        
