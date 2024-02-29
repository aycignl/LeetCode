'''
Author: Gönül Aycı
Email: aycignl@gmail.com
License: MIT, 2024 
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Early return for negative numbers and multiples of 10 (except 0)
        if x < 0 or (x % 10 == 0 and x != 0): return False

        reversed_half = 0

        # Reverse half of the number to compare with the other half
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if the number is palindrome (even- or odd-length)
        return x == reversed_half or x == reversed_half // 10
