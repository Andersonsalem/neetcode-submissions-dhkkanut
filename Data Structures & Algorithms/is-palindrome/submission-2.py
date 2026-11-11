class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = "".join(char.lower() for char in s if char.isalnum())
        maxest = len(s) // 2
        n = len(s)-1
        for i in range(maxest):
            if s[i] != s[n-i]:
                return False

        return True