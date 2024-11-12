prices =[3,4,2,5,7,8]
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1,len(prices)):
        current_prices = prices[i]
        profit = current_prices - min_price

        if profit > max_profit:
            max_profit = profit

        if current_prices < min_price:
            min_price = current_prices

    return max_profit 

print(max_profit(prices))           

    
