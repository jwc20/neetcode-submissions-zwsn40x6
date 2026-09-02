class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in d:  # Character not in s
                return False
            d[t[j]] -= 1
            # if d[t[j]] < 0:  # More occurrences of character in t than in s
            #     return False
        
        
        return True

        
