class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        x = 0

        while x <= 2:
            for i in range(len(nums)):
                ans[i] = nums[i]
            x += 1

        return ans
            
