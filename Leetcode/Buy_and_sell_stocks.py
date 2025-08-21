def buy_and_sell_stocks(prices):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit

num = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stocks(num))