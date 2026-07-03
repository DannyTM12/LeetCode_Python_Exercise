class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, add them, and convert back to binary string
        return str(bin(int(a, 2) + int(b, 2))[2:]) 
    