class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,4]
        
        we can also use two pointers which will give us O(n) time and O(1) space,
        but we can also use hashmaps using a dictionary to achieve O(1) time and O(n) space.


        if using two pointer approach, we will start two pointers (left and right pointers) at index 0 and 1.
        we would increment the right pointers until it reaches the end of the list (len(nums)-1).
        when it reaches the end we would increment the left pointer and right pointer would be set at index: left+1
        if during the loop, the element at left and right pointers are equal, we return true.
        otherwise, the loop keeps going until the left pointer reaches the end of the list.


        The hashmap approach does not need two pointers.
        we would iterate through the list and keep the count of the elements where the key is the element and value is the count of the element in the list.
        we would add a check to see if the count is greater than one.
        if at any point the count is greater than one, return true.
        otherwise, we keep adding all the elements to the hashmap and return false if no count is greater than one.
        """

        count = {}

        for e in nums:
            if e not in count:
                count[e] = 1
            else:
                return True
        
        return False