class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - Naive approach, iterate through array with a running minimum value
            => O(n) time

        Use Binary Search.
        Within the array there are two subarrays that are both monotonic.
        (left and right portions)
        To find the minimum value, we need to find the point where it was rotated.
        That means we need to find the largest of the array (and the minimum)
        To do this, we need to find the largest value of the left portion.

        we need to keep track of the mininum value while applying the binary Search.

        Example: nums = [3,4,5,6,1,2]
        
        [3,4,5,6,1,2]
         l   m     r      

         First, we check if the middle value is in the left or the right portion.
         To do this, we compare the middle `m` value with the left `l` value.

         (nums[m] >= nums[l]) => (5 >= 3)
         This is true, so we know that the middle `m` value is on the left portion.
         We know that the left portion will not contain the minimum value and need to find the rotation point. So we adjust the left pointer => l = mid + 1

        -----------

        [3,4,5,6,1,2]
               l m r

        Check: (nums[m] >= nums[l]) => (1 >= 6). This is False.
        Since it is false, we know that the middle value is now on the right portion.
        Adjust the right pointer.
        r = mid - 1 = 5 - 1 = 4

        -----------

        [3, 4, 5, 6, 1, 2]
                 l,m r
        l = 3, r=4 , m = 3
        So the left pointer `l` and middle pointer `m` is on index 3.
        Check: (nums[m] >= nums[l]) => (6 >= 6). This is True.
        Adjust the left pointer.
        l = mid + 1 = 3 + 1 = 4

        -----------

        [3, 4, 5, 6, 1, 2]
                    l,m,r
        l = 4, r=4 , m = 4
        the left pointer `l`, middle pointer `m`, and the right pointer `r` is on index 4.
        Check: (nums[m] >= nums[l]) => (1 >= 1). This is True.
        Adjust the left pointer.
        l = mid + 1 = 1 + 1 = 2

        
        Now since l <= r is False, we break the loop and return the result.
        which is 1


        ---------------


        Ideas:
        - Do we record the result when nums[m] >= nums[l]?


        """
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                result = min(result, nums[l])
            
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                result = min(result, nums[mid])
                r = mid - 1
                
            else:
                l = mid + 1

        return result

            




