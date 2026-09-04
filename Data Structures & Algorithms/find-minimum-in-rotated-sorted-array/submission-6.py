class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:

            # for cases where there aren't two left and right monotonic portions
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            mid = l + (r - l) // 2
            result = min(result, nums[mid])
            # if the middle value is lesser than or equal to the right value, then we are in the right portion. we should adjust the right value to get the smaller middle value
            if nums[mid] < nums[r]:    
                r = mid - 1
            else:
                l = mid + 1

        return result


