class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l] in alph:
                l += 1
            while r > l and not s[r] in alph:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True