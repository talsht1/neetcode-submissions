class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        if len(s) == 0 or len(s) == 1 : return True
        reversed_string = s[::-1]
        return (s.lower()) == reversed_string.lower()