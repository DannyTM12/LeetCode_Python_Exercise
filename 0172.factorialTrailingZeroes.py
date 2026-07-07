class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        if n < 5: # If n is less than 5, there are no trailing zeroes in the factorial of n, so we return 0
            return 0
        else:

            # While n is greater than 0, we check if n is divisible by 5. 
            # If it is, we count how many times it can be divided by 5 and add that to the count. 
            # We then decrement n by 1 and repeat the process until n is 0. 
            # This will give us the total number of trailing zeroes in the factorial of n.
            while n > 0: 
                if n % 5 == 0: 
                    m = n # We create a variable m to hold the value of n, so we can check how many times it can be divided by 5 without changing the value of n.
                    while m % 5 == 0:
                        m = m // 5 
                        count += 1 
                    n -= 1
                else: 
                    n -= 1
            return count