class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        in: integer array
        out: integer, minimum of the array

        ideas:
        - naive:
            - sort and return 0th elem => O(n log n)
            - two pointers => O(n)

        - Binary Search => O(log n) time 

        - To find the minimum, we need to find the index where the array is rotated.
            - when we find this, we will know that we are at the largest elem and the smallest elem in the list.

        - There are two portions in the array.
            - left and right portion.
            - Since the array is rotated, the smaller elems will on the right while the larger ones on the left.
        - edge case, guard rail check: where the integer array is not rotated

        - We need to apply the binary search and get the middle value,
            - then compare that middle value with the right value.
        - we are trying to find which left or right portion the middle value is currently at.


        - if the middle value is greater than the right value, then it is in the left portion
            - adjust the left pointer

        - if the middle value is lesser than the right value, then it is in the right portion 
            - adjust the right pointer 

        """
        l, r = 0, len(nums) - 1
        result = nums[0] 

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] > nums[-1]:
                
                l = mid + 1
            # elif nums[mid] < nums[-1]:
            else:
                result = nums[mid]
                r = mid - 1
            # else:
                # break 

        return result

            













