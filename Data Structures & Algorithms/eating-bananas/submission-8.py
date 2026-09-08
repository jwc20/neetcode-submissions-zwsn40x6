from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        in: array of integers and total hours to eat all piles
        out: integer, the minimum rate of eating to eat all piles

        Ideas:
        - This problem can be solved naively using a simple loop with a running minimum rate to eat all piles.
            - This will take O(n) time where n is the length of the array and constant space
        
        - The Binary Search approach can reduce the time to O(log n)
        - where the B.S. is applied to the rates to eat the piles.
            - the minimum rate would be 1
            - the max would be the value of the largest pile.
        
        Example:
        piles = [1,4,3,2], h = 9

        Here we would apply binary search to the rate of eating from 1 to 4.
        -> [1, 2, 3, 4]
            l  m     r 

        we would get the middle value eating speed, and use that to get the total hours to eat all the bananas.
        Then compare that value with the input total hours `h`
        While applying the B.S. we keep a running minimum value to return as result.


        -> [1, 2, 3, 4],         h = 9
            l  m     r         m=2 => tt=(1+1+2+2)=6 < 9 = h    minimum_eating_rate=2
               l. m. r         m=3 => tt=(1+1+1+2) = 5 <9
                 l,m r         m=  => tt=4 < 9


        piles=[3,6,7,11].      h=8

        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
         l              m                r.    tt=1+1+2+2=6 < 8.  res=6
                           l     m       r   

        """
        l, r = 1, max(piles)
        minimum_eating_rate = r

        while l <= r:
            k = l + (r - l) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / k)


            if total_hours <= h:
                minimum_eating_rate = k                
                r = k - 1
            else:   
                l = k + 1

        return minimum_eating_rate
            

            













