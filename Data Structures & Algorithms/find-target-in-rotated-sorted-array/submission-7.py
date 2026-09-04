class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        ideas:
        - we need to find the pivot point, where the array rotates
        - need to compare to find where the target is (in the left or right portion) using the pivot point
        """

        l, r = 0, len(nums) -1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 

        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1


        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid

        return -1
