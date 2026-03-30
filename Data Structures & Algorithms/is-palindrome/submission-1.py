class Solution:
    def isPalindrome(self, s: str) -> bool:
        # should also remove non alphanumeric characters
        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j: # A single letter is palindrome by itself

            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1
                
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True