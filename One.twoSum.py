class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashTable = {}  # Create a hash table to store the indices of the numbers

        for i in range(len(nums)):     #  Iterate through the list of numbers
            complement = target - nums[i]  # Calculate the complement of the current number
            if complement in hashTable:  # Check if the complement exists in the hash table
                return [i, hashTable[complement]]  # If it does, return the indices of the current number and its complement
            hashTable[nums[i]] = i    # Store the index of the current number in the hash table
        return []  # If no solution is found, return an empty list