import re  # Importing the regular expression module to use regex for string manipulation

class Solution:
    def isPalindrome(self, s: str) -> bool:   
        new_s = re.sub('[^a-zA-Z0-9]', '', s).lower()  # Using regex to remove all non-alphanumeric characters from the string and converting it to lowercase for uniformity
        return new_s == new_s[::-1]  # Checking if the cleaned string is equal to its reverse, which determines if it is a palindrome

