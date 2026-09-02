class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Ideas:
            - we need to remove the punctuations and white spaces
            - use two pointers from the opposite side
                - loop until l < r
            - lower case all characters in the string
        """
        ns = s
        ns = ns.lower()
        ns = ns.split(" ")
        ns = "".join(ns)

        # punctuations = ".,!?'"
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        s_length = len(ns)
        for i in range(s_length):
            if ns[i] not in alphabet:
                ns = ns.replace(ns[i], "")
                # s_length -= 1



        print(ns)
        
        
        l, r = 0, len(ns) - 1
        

        while l < r:
            # while l < r and s[l] not in alphabet:
            #     l += 1
            # while l < r and s[r] not in alphabet:
            #     r -= 1
            
            if ns[l] != ns[r]:
                return False
            else:
                l, r = l + 1, r - 1

        return True
            
        
