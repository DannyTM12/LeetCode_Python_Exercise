class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split() # Split the string into words and remove leading/trailing spaces

        return len(s[-1]) # Return the length of the last word