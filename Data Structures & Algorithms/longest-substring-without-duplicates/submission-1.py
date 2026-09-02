
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_length = 1
        window_start = 0
        

        for window_end in range(1, len(s)):
            c1 = s[window_start]
            c2 = s[window_end]

            if s[window_end] == s[window_end - 1]:  # instead of this do window + 1
                window_start, window_end = window_end, window_end + 1

            # adjust the window start
            else:
                max_length = max(max_length, window_end - window_start)
                while window_start < window_end and s[window_end] == s[window_start]:
                    window_start += 1

        return max_length