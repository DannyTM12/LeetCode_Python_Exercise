class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        return y == y[::-1]  # Check if the string representation of the number is equal to its reverse