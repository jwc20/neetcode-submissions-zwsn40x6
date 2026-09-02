class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower().split(" ")
        l, r = 0, len(a) - 1
        alph = "abcdefghijklmnopqrstuvwxyz"
        while l < r:
            if a[l] != a[r]:
                return False
            elif a[l] not in alph:
                l += 1
            elif a[r] not in alph:
                r -= 1
            
        return True