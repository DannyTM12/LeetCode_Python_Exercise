class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: # If the last digit is not 9, we can just sum 1 to it and return the array
            digits[-1] += 1
            return digits
        else: # If the last digit is 9, we need to sum 1 to
            new_s = "" # Create a new empty str to save all the digits of the array

            for i in range(len(digits)):  # Iterate the array until the string is filled with all the digits
                new_s = new_s + str(digits[i]) # Append every digit in the array as a string
        
            new_s = str(int(new_s) + 1) # Transform the string into an int to sum 1, and back to an string

            digits = [] # Clean out the array so we can fulfill again

            for j in range(len(new_s)): # Iterarte the string with the new sum
                digits.append(int(new_s[j])) #Fill the original array with every element of the string converted in an int

        return digits