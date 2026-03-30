class Solution:
    def isPalindrome(self, s: str) -> bool:
        # should also remove non alphanumeric characters
        i, j = 0, len(s) - 1
        s = s.lower()
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
                
            if not s[j].isalnum():
                j -= 1
                continue
                
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True