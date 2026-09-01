class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        Ideas:
        - we dont know how many times the nums list was rotated
        - we want the minimim value in the list
    
        - Naive Approach:
            - we need to have an algorithm that runs in O(log n) time
                - can't use `min()` or `sorted()`
                    - sort the array using `sorted()` -> O(n log n)
                    - then get the `nums[0]`

            - we can't use an algorithm that runs in O(n) time
                - can't use two pointers method

        - Binary search
            - apply binary search

        - we want the minimum value on the left and the maximum value on the right    
        """
        result = nums[0]
        l, r = 0, len(nums) -1 

        while l <= r:
            if nums[l] < nums[r]:
                result = min(nums[l], result)
                break

            mid = (l + r) // 2
            result = min(nums[mid], result)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return result











