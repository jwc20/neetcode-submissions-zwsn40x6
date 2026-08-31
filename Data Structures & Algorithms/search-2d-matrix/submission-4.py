class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Ideas:
        - two binary search is used:
            - to find which row the target value is, and 
            - to find the target value in the list
        - this will give us time of O(log(m) + log(n)) which turns out to be O(log(m * n)) with no additional space used -> O(1)

        - One-pass binary search can be used but it can be hard to implement in interviews, does not necessarily have advantages over the two-pass method above
        """

        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = top + ((bot - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot): return False

        row = top + ((bot - top) // 2)
        l, r = 0, cols - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


