class Solution:

    def isPalindrome(self, s: str) -> bool:
        def alphanumeric(ch):
            if (ord('a') <= ord(ch) <= ord('z')
                or ord('A') <= ord(ch) <= ord('Z')
                or ord('0') <= ord(ch) <= ord('9')):
                return True
            
            return False

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not alphanumeric(s[l]):     
                l += 1
            
            while l < r and not alphanumeric(s[r]):
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True