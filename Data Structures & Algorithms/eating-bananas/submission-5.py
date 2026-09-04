from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Ideas:
        - the piles array is not monotonic
        - eating from pile, need to get the ceiling of pile / eating rate
        - we need to get the total time to eat all the bananas and compare that value to the `h` value

        we can do this naively and start from eating rate of 1 and increase the value from there and get the minimum value.


        For example: piles = [1,4,3,2], h = 9

        - set `k` = 1, then total_time = 1 + 4 + 3 + 2 = 10 hours to eat.
            - compare with h => not valid
        
        - set `k` = 2, then total_time = 1 + 2 + 2+ 1 = 6
            - compare with h =>  valid
                - set `result` = 6

        - set `k` = 3, then total_time = 1 + 2 + 1+ 1 = 5
            - compare with h => valid
                - set `result` = 5

        - and so on ...


        a better approach would be to use binary search and start the eating rate at the middle.
        To find the middle, we need to find the range.
            - the minimum will always be 1
            - the maximum will be the largest value in the array
                => max(piles)
        Using those two values as the left and right pointers, we can apply the binary search.

        l, r = 1, max(piles)

        We also need to keep track of the minimum value to return as result.
        """
        result = piles[0]
        l, r = 1, max(piles)

        while l <= r:
            # need to get the total time to eat the bananas
            total_time = 0
            k = (l + r) // 2

            for pile in piles:
                total_time += ceil(pile/k)

            if total_time <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
                

        return result

            

















