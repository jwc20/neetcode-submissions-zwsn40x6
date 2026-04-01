class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Ideas:
            - we need to remove the punctuations and white spaces
            - use two pointers from the opposite side
                - loop until l < r
            - lower case all characters in the string
        """

        # s = s.lower()
        # s = s.split(" ")
        # s = "".join(s)

        # # punctuations = ".,!?'"
        # alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        # for i in range(len(s)):
        #     if s[i] not in alphabet:
        #         s = s.replace(s[i], "")

        # print(s)
        
        
        l, r = 0, len(s) - 1
        

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
            
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        
