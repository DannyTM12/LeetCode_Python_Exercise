class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # Maximum profit found so far and initialized to 0
        min_buy = float('inf') # Minimum buying price found so far and initialized to infinity
        for i in range(len(prices)): # Iterate through each price
            min_buy = min(min_buy, prices[i]) # Update the minimum buying price if the current price is lower
            max_profit = max(max_profit, prices[i] - min_buy) # Update the maximum profit if the current profit is higher
        return max_profit # Return the maximum profit found and always is minimum 0