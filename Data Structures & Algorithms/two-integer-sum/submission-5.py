class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The naive approach would be to use double loop to check all two sums and checking with the target value.
        This will take O(n^2) time and O(1) space.

        A better approach would be to use two pointers to avoid using double loop.
        We would have to have pointers starting at the start and end (index 0 and len(nums)-1) and compare the sums at the pointer with the target.
        if the sum is greater, decrement the right pointer.
        if he sum is lesser, increment the left pointer.
        if the sum matches the target, we return the indices.

        However, the problem does not state if this the input list is sorted.
        Assuming it is not sorted, the time complexicity will be O(nlogn) and O(1) space.

        Using a hashmap would give us better time comp. at the cost of taking up memory (O(n) space).
        We can use a hashmap to store the indicises as key and value as the element.
        Then we can loop over the hashmap values and check if the target minus the current value is in the hashmap.
        
        ----------------------------

        nums = [3,4,5,6], target = 7

        # 1. create hashmap

        hashmap = {
            1: 3
            2: 4
            3: 5
            4: 6
        }

        hashmap = {
            3: 1
            4: 2
            5: 3
            6: 4
        }

        # 2. loop over the nums array, check target - current element

        for element in [3,4,5,6]:
            if target - element is in hashmap:
                return [hashmap[element], hashmap[target - element]]


        -----------------------

        IDEAS:
        - are there any edge cases?
            - empty array 
            - array with only one value

        but these we are assuming every input has exactly one pair of result [i,j].
        """

        # hashmap = {}

        # for index, elem in enumerate(nums):
        #     hashmap[elem] = index

        # for index, elem in enumerate(nums):
        #     diff = target - elem
        #     if diff in hashmap and hashmap[diff] != index:
        #         return [index, hashmap[diff]]


        prevmap = {}

        for index, elem in enumerate(nums):
            diff = target - elem

            if diff in prevmap:
                return [prevmap[diff], index]
            prevmap[elem] = index










        