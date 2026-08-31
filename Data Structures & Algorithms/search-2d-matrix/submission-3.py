class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

        [[1, 2, 4, 8],
         [10,11,12,13],
         [14,20,30,40]]

        Ideas:
        - the left and right pointers will operate inside each list inside the matrix
        - how to check which lists to use binary search on?
            
            - check the last elem in the list (the highest value) and compare with the target?
                - just iterate through each items in the matrix.

        
        This approach is not optimal because the time is O(m + log(n))

        we want O(log(m) + log(n))
        """

        for row in matrix:
            if row[-1] < target:
                continue
            else: 
                l, r = 0, len(row) - 1

                while l <= r:
                    mid = l + ((r - l) // 2)

                    if target > row[mid]:
                        l = mid + 1
                    elif target < row[mid]:
                        r = mid - 1
                    else:
                        return True
                return False
        return False

                