class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Ideas:
            - we need to remove the punctuations and white spaces
            - use two pointers from the opposite side
                - loop until l < r
            - lower case all characters in the string
        """

        s = s.lower()
        s = s.split(" ")
        s = "".join(s)

        # punctuations = ".,!?'"
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(len(s)):
            if s[i] not in alphabet:
                s = s.replace(s[i], "")

        print(s)
        
        
        l, r = 0, len(s) - 1
        

        while l < r:
            # while l < r and s[l] not in alphabet:
            #     l += 1
            # while l < r and s[r] not in alphabet:
            #     r -= 1
            
            if s[l] != s[r]:
                return False
            else:
                l, r = l + 1, r - 1

        return True
            
        
