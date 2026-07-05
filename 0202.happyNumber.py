class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {} # Create a hashmap to save the numbers we have seen so far

        while n not in seen: # Iterate until we find a number that we have seen before
            if n == 1:     # If we reach 1, then we have found a happy number
                return True
            
            seen[n] = True  # We save the number we have seen so far in the hashmap

            new_n = 0  # Initialize the new number

            for i in range(len(str(n))):  # Iterate through the digits of the number and calculate the sum of the squares of its digits
                new_n += int(str(n)[i])**2 

            n = new_n # Update n to the new number we have calculated
        
        return False