# You are given an array. Each element represents the price of a stock on that particular day. 
# Calculate and return the maximum profit you can make from buying and selling that stock only once.

# Input  : [44, 30, 24, 32, 35, 30, 40, 80, 5]
# Output : 56
# Here, the optimal trade is to buy when the price is 24, and sell when it is 80, so the return value should be 56 (profit = 80 - 24 = 56).

def buy_and_sell(arr): 
	lowest_prices = [l for l in sorted(arr)]
	earnings = []
	for i in lowest_prices:
		price_after_lowest = arr[arr.index(i):]
		highest_price = sorted(price_after_lowest)[-1]
		earnings += [highest_price - i]
	return sorted(earnings)[-1]

print(buy_and_sell([44, 30, 24, 32, 35, 30, 40, 80, 5])) 