class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # Initialize a pointer to keep track of the position to insert non-val elements


        for num in nums: # Iterate through each element in the input list
            if num != val:  # If the current element is not equal to the value to be removed, we keep it in the list
                nums[i] = num # Assign the current element to the position indicated by the pointer i
                i += 1 # Increment the pointer i to the next position for the next non-val element

        return i # Return the new length of the modified list, which is the count of non-val elements