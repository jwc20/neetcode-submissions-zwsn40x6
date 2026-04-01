class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """

        In Python, we can use the sort function to sort the string (a-z) and then we can use pointers at the start of both strings 
        and compare each characters. 
        This will take O(nlogn) + O(n) time which is approximately O(nlogn) time with O(1) space.

        If we are allowed to take additional memory space, we can use a hashmap to achieve O(n) time and space.
        First, we would iterate string `s` and during, we can store each element into a dictionary or set as key and the count of the character as value.

        After looping over string `s`, we can loop over string `t` and decrement each occurrence of the character. 
        If the character in `t` is not in the hashmap, then we return false.

        after the loop over string `t` is over, we need to check if all the values in the hashmap are 0.
        if not, return false.


        ---------------

        s = "racecar", 
        t = "carrace"

        loop 1: loop over s = "racecar"   

        dict = {
            r:2
            a:2
            c:2
            e:1
        }



        loop 2: loop over t = "carrace"

        dict = {
            r:0
            a:0
            c:0
            e:0
        }

        return true

        ---------------

        NOTE: 
        - we can use the all() method and list comprehension to check if all values are 0
        """

        # edge case
        if len(s) != len(t):
            return False


        dict = {}

        for e in s:
            if e not in dict:
                dict[e] = 1
            else:
                dict[e] += 1
        
        for e in t:
            if e not in dict:
                return False
            else:
                dict[e] -= 1
                if dict[e] < 0:
                    return False

        if all(e == 0 for e in dict.values()):
            return True
        return False


    