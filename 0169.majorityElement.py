class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0 # This will count the majority element    
        candidate = 1 # This arbitrary value will change in function of the count value.

        # Moores algorithm: If the count is 0, we change the candidate to the current number. If the current number is equal to the candidate, we increment the count. Otherwise, we decrement the count.
        for num in nums:
            if count == 0: # If the count is 0, we change the candidate to the current number
                candidate = num

            if num == candidate: # If the current number is equal to the candidate, we increment the count
                count += 1
            else: # Otherwise, we decrement the count
                count -= 1
        return candidate # At the end of the loop, the candidate will be the majority element