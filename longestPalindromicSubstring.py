'''
Author: Gönül Aycı
Email: aycignl@gmail.com
License: MIT, 2024 
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base case check
        if len(s) <= 1: return s
        # Initialize 'longest_palindrome' to the first character of 's'
        longest_palindrome = s[0]

        for i in range(len(s) - 1):
            odd_palindrome = self._expandAroundCenter(s, i, i)
            even_palindrome = self._expandAroundCenter(s, i, i + 1)

            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome

    def _expandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1 # Move 'left' backwards
            right += 1 # Move 'right' forwards

        return s[left + 1:right]
