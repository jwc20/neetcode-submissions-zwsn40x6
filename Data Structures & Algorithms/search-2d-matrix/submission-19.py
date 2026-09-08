class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        in:  matrix (array of integer arrays) and a target value
        out: boolean

        Ideas:
        - two binary search is needed
            - one for getting which row has the target value
            - and another for finding the actual target value in the row 
        

        Example:

        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

        [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
            top       row         bot 
        
        - Apply the first binary search where the middle row is called row 
            - row = (top + bot) // 2
        - So we can find which row contains the target value 
            - by comparing the first and the last value of the rows.
        - It should satisfy this logic: matrix[row][0] < target < matrix[row][-1]


        10 <= target <= 13

        This is true, so the target value is inside this row.

        
        Afterwards, we apply the second binary search to find the target value within the row.
        """
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = top + (bot - top) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break 
        
        row = top + (bot - top) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False




