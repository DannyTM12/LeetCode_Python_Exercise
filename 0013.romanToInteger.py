class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Create a hash map to store the values of Roman numerals
        hashmap = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50,'C' : 100, 'D' : 500, 'M' : 1000} 

        result = 0 # Initialize the result variable to store the final integer value

        # Iterate through the string of Roman numerals
        for i in range(len(s)):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i + 1]]: # Check if the current numeral is less than the next numeral
                result -= hashmap[s[i]] # If it is, subtract the value of the current numeral from the result
            else:
                result += hashmap[s[i]] # If it is not, add the value of the current numeral to the result
        # Return the final result after processing all the numerals
        return result