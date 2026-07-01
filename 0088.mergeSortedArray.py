class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        #Declare three pointers for nums1, nums2, and the merged array
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0: # Iterate until all elements from nums2 are merged
            if i >= 0 and nums1[i] > nums2[j]: # If the current element in nums1 is greater than the current element in nums2, place it in the merged array
                nums[k] = nums1[i] # Place the larger element in the merged array
                i -= 1 # Move the pointer for nums1 to the left
            else:  # If the current element in nums2 is greater than or equal to the current element in nums1, place it in the merged array
                nums[k] = nums2[j]  # Place the larger element in the merged array
                j -= 1  # Move the pointer for nums2 to the left
            k -= 1  # Move the pointer for the merged array to the left