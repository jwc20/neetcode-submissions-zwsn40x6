class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        ideas:

        The Naive approach would be to apply brute force and loop/iterate through every subarray in matrix and apply another loop to find the target value.
        This will take O(n+m) time where the n is length of `matrix`(or rows) and m is the length of the subarrays(or columns).

        A better approach would be to use binary search two times, first to determine which row the target value is at, then find the target value within that row.
        This will take O(log n + log m) time which is O(log (m+n)) time approximately.

        To find which row(subarray in `matrix`) is holding the target value, we can compare the last value of the subarray with the target value. Since the `matrix` value is monotonically increasing, the last values of the subarrays will be the greatest in the array.

        For example, in matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        In the first row [1,2,4,8], we check the target value (target=10) with the last value in the row, which is 8.
        Since the target value is greater (target = 10 > 8 = arr[-1]), we dont need to check the elements in the left side of the last value of the array (we dont need to check element 1, 2, 4 in [1,2,4,8])

        * row's last element is greater than the target => move the left pointer to the middle + 1
        * row's last element is lesser than the target => move the right pointer to the middle - 1

        after finding which row is likely to hold the target value, apply another binary search to search for the target value.


        [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        
        l=0, r=2, row=1       
        target = 10 >=! 13 = matrix[row][-1] 
            => r = row = 1
        
        l=0, r=1, row=0
        target = 10 >= 8 = matrix[row][-1] 
            => l = row + 1 = 0 + 1 = 1
        
        l=1, r=1, row=1
        target = 10 >= 13 = matrix[row][-1] 
            => r = row = 1
        



        """
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False


        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
