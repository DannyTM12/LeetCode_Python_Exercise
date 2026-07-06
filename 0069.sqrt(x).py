class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: # If x is 0 or 1, the square root is x itself
            return x
        else:
            lo = 1 # Start from 1 since we already handled 0 and 1
            hi = x // 2 # The square root of x cannot be greater than x // 2 for x > 1

            # Use binary search to find the integer square root
            while lo <= hi: # Continue searching while the lower bound is less than or equal to the upper bound
                mid = (lo + hi) // 2 # Calculate the middle point
                if mid*mid == x: # If mid squared equals x, we found the exact square root
                    return mid
                elif mid*mid < x: # If mid squared is less than x, we need to search in the upper half
                    lo = mid + 1
                else: # If mid squared is greater than x, we need to search in the lower half
                    hi = mid - 1 
            return hi # After the loop, hi will be the largest integer such that hi*hi <= x, which is the integer square root of x.