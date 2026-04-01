class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Ideas:
            - have a dictionary where the key is the elements and the values are the positions in the list.
            - loop over the list checking if the difference of the target and the current value exists in the dictionary.
            => O(n) space and time where n is the length of the input nums.
        """

        d = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[target - n], i]
            d[n] = i
